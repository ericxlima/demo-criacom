import os
from PIL import Image
from dotenv import load_dotenv
import qrcode

import cloudinary
import cloudinary.uploader
import cloudinary.api

load_dotenv()

cloudinary.config(
    cloud_name=os.environ.get("CLOUD_NAME"),
    api_key=os.environ.get("API_KEY"),
    api_secret=os.environ.get("API_SECRET")
)


def create_qr_code(image_path: str):
    response = cloudinary.uploader.upload(image_path, folder="demo_criacom")

    if response:
        image_link = response['secure_url']
        qr = qrcode.make(image_link)
        qr_filename = f"qr_code_{image_path.split('/')[-1]}.png"
        qr.save(qr_filename)
    else:
        print("Falha no upload da imagem:", response.text)


def make_collage(path_img1, path_img2, uuid, altura_final=1024):
    imagem1 = Image.open(path_img1)
    imagem2 = Image.open(path_img2)

    largura_colagem = min(imagem1.width, imagem2.width)

    proporcao = largura_colagem / imagem1.width
    nova_altura_imagem1 = int(imagem1.height * proporcao)
    imagem1 = imagem1.resize((largura_colagem, nova_altura_imagem1))

    altura_total = nova_altura_imagem1 + imagem2.height

    altura_colagem = min(altura_total, altura_final)

    imagem_final = Image.new("RGB", (largura_colagem, altura_colagem), "white")

    imagem_final.paste(imagem1, (0, 0))

    posicao_imagem2 = nova_altura_imagem1
    if posicao_imagem2 < altura_colagem:
        imagem_final.paste(imagem2, (0, posicao_imagem2))

    imagem_final.save(f"images/ARENA IA - CIn - Colagens/{uuid}_collage.jpg")
    print(f"Colagem criada e salva como '{uuid}_collage.jpg'")


if __name__ == "__main__":
    # create_qr_code("/home/ericxlima/Documents/demo-criacom/images/demo.png")
    pass