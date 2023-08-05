import os
def allowed_names(pasta):
    extensoes_validas = ['.jpg', '.jpeg', '.png', '.webp']
    nomes_fotos = []

    for arquivo in os.listdir(pasta):
        _, extensao = os.path.splitext(arquivo)
        if extensao.lower() in extensoes_validas:
            nomes_fotos.append(arquivo[0:arquivo.find('.')])

    return nomes_fotos
