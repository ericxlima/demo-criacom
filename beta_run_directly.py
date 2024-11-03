import torch
import os
from huggingface_hub import HfApi
from pathlib import Path
from diffusers.utils import load_image
from PIL import Image
import numpy as np
from controlnet_aux import PidiNetDetector, HEDdetector

from diffusers import (
    ControlNetModel,
    StableDiffusionControlNetPipeline,
    UniPCMultistepScheduler,
)

import gradio as gr
import cv2
import numpy as np
from PIL import Image
from gradio_client import Client
import os
import uuid

checkpoint = "lllyasviel/control_v11p_sd15_scribble"

processor = HEDdetector.from_pretrained('lllyasviel/Annotators')

controlnet = ControlNetModel.from_pretrained(checkpoint, torch_dtype=torch.float16)

pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", controlnet=controlnet, torch_dtype=torch.float16
)

pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()

def create_directory(directory_name='images'):
  try:
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created successfully.")
  except FileExistsError:
    print(f"Directory '{directory_name}' already exists.")
  except PermissionError:
    print(f"Permission denied: Unable to create '{directory_name}'.")
  except Exception as e:
    print(f"An error occurred: {e}")

def create_image(image_path):
  image = load_image(image_path)
  print(type(image))
  prompt = "a picture of a stuffed animal, best quality, extremely detailed, plush, felt, face, lifelike, simple background, plain background" # "A stuffed animal, plain background, face"
  control_image = processor(image, scribble=True)
  generator = torch.manual_seed(0)
 
  n_prompt = "longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, hands, flesh, skin, human, glass, sky, plant, faceless, paint, pillow, complex background" # "complex background, faceless"
 
  image2 = pipe(prompt, num_inference_steps=22, generator=generator, image=control_image, negative_prompt=n_prompt, guidance_scale=12).images[0]
 
  image_uuid = str(uuid.uuid4())

  image.save('images/' + image_uuid + 'original.png')
  image2.save('images/' + image_uuid + '.png')
 
  return image2

create_directory()

iface = gr.Interface(
    # fn=process_image,
    fn=create_image,
    inputs=gr.Image(type="filepath", label="Tire uma foto"),
    outputs=gr.Image(label="Imagem processada"),
    live=False,
    title="",
    css="""
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700&display=swap');

        .gradio-container {
            font-family: 'Nunito', sans-serif;
            background: linear-gradient(#000000 25%, #ff0571 75%, #f98404); # verde 1eff05, laranja f98404, roxo 52057b, rosa ff0571
            color: #ffffff;
            text-align: center;
        }
        h1 {
            width: 100%;
            margin-top: -30px;
            max-width: 300px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    """
)

# Inicia a interface
iface.launch(debug=True)