import cv2
from simple_facerec import SimpleFacerec
from NomesPermitidos import allowed_names

# Indíce da Webcam
index_webcam = 0

# Codifica as faces da pasta
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Carrega a câmera
cap = cv2.VideoCapture(index_webcam)

# Obtém nomes permitidos
images = r"CAMINHO/PARA/PASTA/IMAGES"
allowed_names = allowed_names(images)

last_name = ''

while True:
    ret, frame = cap.read()

    # Detecta as faces
    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        if name != last_name:
            if name in allowed_names:
                print('ACESSO CONCEDIDO!')
            else:
                print('ACESSO NEGADO!')

        last_name = name

        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()





