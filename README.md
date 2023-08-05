# Detector Facial com integração do Arduino
Este projeto em Python oferece uma solução completa para detecção facial, permitindo a análise de imagens em uma pasta e o reconhecimento de rostos em tempo real através da webcam. A detecção facial é realizada por meio da biblioteca OpenCV, que é amplamente utilizada para tarefas de visão computacional.

A primeira parte do projeto explora o uso da webcam para realizar a detecção de rostos em tempo real. Ao executar esse código, a webcam é ativada, e o programa utiliza a abordagem de detecção facial do OpenCV para identificar e destacar os rostos presentes na cena em tempo real. Isso possibilita que os rostos sejam identificados em tempo real enquanto aparecem na webcam. Rostos não conhecidos, ou seja, os rostos que não foram colocados na pasta "images" serão destacados como "Desconhecido" enquanto os demais terão o seu nome destacado.

Para garantir uma maior segurança e controle de acesso, o projeto também conta com integração com um dispositivo Arduino. Um segundo código Python foi desenvolvido para realizar a comunicação entre o programa de detecção facial e o Arduino. Nesse código, o usuário pode definir uma lista de rostos permitidos, ou seja, rostos previamente cadastrados e autorizados a ter acesso.

A lógica de integração é simples: caso um rosto permitido seja detectado pela webcam, o código envia um sinal para o Arduino, que pode ser um sinal luminoso, sonoro ou qualquer outro tipo de dispositivo conectado ao Arduino. Da mesma forma, caso um rosto não autorizado seja detectado, o Arduino pode emitir um alerta, sinalizando a presença de uma pessoa não autorizada.


# Utilização

CERTIFIQUE-SE DE TER UMA WEBCAM

Primeiramente, baixe as seguintes bibliotecas:

1) cv2 (OpenCV)
2) face_recognition
3) os
4) glob
5) numpy
6) pyfirmata (Caso deseje integrar com o Arduino)

Feito isso, coloque os códigos, "DeteccaoFacial.py", "IntegracaoArduino.py", "NomesPermitidos.py", "simple_facerec.py" na mesma pasta.
   
Crie uma pasta chamada "images" no mesmo diretório dos códigos. Nessa pasta, coloque fotos dos rostos de pessoas que você deseja reconhecer, o nome das imagens precisam ser o nome das pessoas presentes nas imagens.

Após isso, basta rodar o código.




