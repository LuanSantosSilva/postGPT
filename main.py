from classes.Content import Content
from classes.ImagePost import ImagePost
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.environ['API_KEY']
content = Content(KEY)

# GERANDO O TEXTO DA IMAGEM
content = Content(KEY)
texto_post = content.content_txt_gpt('Cite uma curiosidade aleatória correta, completa, com evidências e com fontes confiáveis (obs: sem ser url, cite apenas o nome) tudo em isso formulado em um parágrafo da forma mais resumida possível')

texto_post = content.wrap_text(texto_post)

# GERANDO A DESCRICAO DO POST
descricao = content.content_txt_gpt(f'Gere uma descrição pro Instagram sobre esse texto: {texto_post}')
print(descricao)
desc_img = content.content_txt_gpt(f'Gere uma descrição pro Dall-e criar uma imagem sobre esse texto: {texto_post}')

# GERANDO A IMAGEM PRINCIPAL
background_post = content.content_img(desc_img)

image = ImagePost()
back = image.save_web_img(background_post)
img1 = image.img_blur()
img2 = image.color_slayer()
img3 = image.join_slayer(img1, img2)
post = image.write_img(img3, texto_post)
image.save_pil_img(post)

