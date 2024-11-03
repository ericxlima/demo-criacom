from PIL import Image

def make_collage(path_img1, path_img2, uuid, altura_final=1024):
    # Carregar as duas imagens
    imagem1 = Image.open(path_img1)
    imagem2 = Image.open(path_img2)

    # Definir a largura da colagem como a largura da menor imagem
    largura_colagem = min(imagem1.width, imagem2.width)

    # Redimensionar a primeira imagem para a largura da menor imagem, mantendo o aspecto
    proporcao = largura_colagem / imagem1.width
    nova_altura_imagem1 = int(imagem1.height * proporcao)
    imagem1 = imagem1.resize((largura_colagem, nova_altura_imagem1))

    # Calcular a altura total necessária para a colagem
    altura_total = nova_altura_imagem1 + imagem2.height

    # Determinar a altura da colagem com base no parâmetro `altura_final`
    altura_colagem = min(altura_total, altura_final)

    # Criar uma nova imagem com a largura da menor imagem e altura especificada
    imagem_final = Image.new("RGB", (largura_colagem, altura_colagem), "white")

    # Colar a primeira imagem no topo da colagem
    imagem_final.paste(imagem1, (0, 0))

    # Colar a segunda imagem logo abaixo da primeira, se houver espaço suficiente
    posicao_imagem2 = nova_altura_imagem1
    if posicao_imagem2 < altura_colagem:
        imagem_final.paste(imagem2, (0, posicao_imagem2))

    # Salvar o resultado no diretório especificado com o UUID fornecido
    imagem_final.save(f"images/ARENA IA - CIn - Colagens/{uuid}_collage.jpg")
    print(f"Colagem criada e salva como '{uuid}_collage.jpg'")

make_collage("images/2c83d100-0d8d-4983-82da-7c0a7df723c7original.png", "images/2c83d100-0d8d-4983-82da-7c0a7df723c7.png", "2c83d100-0d8d-4983-82da-7c0a7df723c7", 1024)
