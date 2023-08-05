import cv2
from time import sleep
from pyfirmata import Arduino
from simple_facerec import SimpleFacerec
from NomesPermitidos import allowed_names


# Codifica as faces da pasta
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Carrega a câmera
cap = cv2.VideoCapture(0)

# Estabelece conexão com o Arduino
Uno = Arduino('COM3')

# Obtém nomes permitidos
images = r"C:\Users\breno\PycharmProjects\ReconhecimentoFacial\images"
allowed_names = allowed_names(images)

# Roda o código de detecção
while True:
    ret, frame = cap.read()

    # Detecta as faces
    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        if name in allowed_names:
            print('ACESSO CONCEDIDO!')

            # Envia um sinal de HIGH para a porta 13 digital do Arduino
            Uno.digital[13].write(1)
            sleep(10)

        else:
            print('ACESSO NEGADO!')

            # Envia um sinal de LOW para a porta 13 digital do Arduino
            Uno.digital[13].write(0)

        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        # Envia um sinal de LOW para a porta 13 digital do Arduino. Fiz isso pois o Arduino, no meu caso, foi usado para abrir e fechar uma porta, dessa forma,
        # estabeleci um tempo de 10 segundos para a fechadura fechar depois de abrir.
        Uno.digital[13].write(0)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break


# Finaliza o código
cap.release()
cv2.destroyAllWindows()






