from PIL import Image

# Carregar as duas imagens
imagem1 = Image.open("images/1o.png")  # Imagem 1920x1440
imagem2 = Image.open("images/1g.png")  # Imagem 704x512

# Redimensionar a primeira imagem para 704px de largura, mantendo o aspect ratio
nova_largura = 704
proporcao = nova_largura / imagem1.width
nova_altura = int(imagem1.height * proporcao)
imagem1 = imagem1.resize((nova_largura, nova_altura))

# Calcular a altura total para a colagem (precisamos de 1024 de altura)
altura_total = 1024

# Criar uma nova imagem com 704x1024 e fundo branco
imagem_final = Image.new("RGB", (nova_largura, altura_total), "white")

# Colar a primeira imagem no topo da imagem final
imagem_final.paste(imagem1, (0, 0))

# Colar a segunda imagem logo abaixo da primeira
imagem_final.paste(imagem2, (0, imagem1.height))

# Salvar o resultado
imagem_final.save("images/ARENA IA - CIn - Colagens/colagem_final.jpg")
