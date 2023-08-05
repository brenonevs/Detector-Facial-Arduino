# Detector Facial com integração do Arduino
Este projeto em Python oferece uma solução completa para detecção facial, permitindo tanto a análise de imagens em uma pasta quanto o reconhecimento de rostos em tempo real através da webcam. A detecção facial é realizada por meio da biblioteca OpenCV, que é amplamente utilizada para tarefas de visão computacional.

A primeira parte do projeto explora o uso da webcam para realizar a detecção de rostos em tempo real. Ao executar esse código, a webcam é ativada, e o programa utiliza a abordagem de detecção facial do OpenCV para identificar e destacar os rostos presentes na cena em tempo real. Isso possibilita que os rostos sejam identificados em tempo real enquanto aparecem na webcam.

Para garantir uma maior segurança e controle de acesso, o projeto também conta com integração com um dispositivo Arduino. Um segundo código Python foi desenvolvido para realizar a comunicação entre o programa de detecção facial e o Arduino. Nesse código, o usuário pode definir uma lista de rostos permitidos, ou seja, rostos previamente cadastrados e autorizados a ter acesso.

A lógica de integração é simples: caso um rosto permitido seja detectado pela webcam, o código envia um sinal para o Arduino, que pode ser um sinal luminoso, sonoro ou qualquer outro tipo de dispositivo conectado ao Arduino. Da mesma forma, caso um rosto não autorizado seja detectado, o Arduino pode emitir um alerta, sinalizando a presença de uma pessoa não autorizada.
