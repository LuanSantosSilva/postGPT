from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
import os
class ImagePost():
    def __init__(self):
        self.img_save = None
        self.image = None
        self.folder_img = None
        self.NAME_FOLDER_IMGS = 'imgs'

        self.__folder()

    def __folder(self):
        """ Essa função verifica se um determinado diretório já foi criado. Caso não tenha sido, ela mesmo cria. """
        main_path = os.getcwd()
        imgs = os.path.join(main_path, self.NAME_FOLDER_IMGS)
        diretorio = [imgs]
        for path in diretorio:
            if(os.path.isdir(path)):
                pass
            else:
                os.mkdir(path)

        self.folder_img = imgs
        return self.folder_img

    def save_web_img(self, url:str, name_img:str='index.png'):
        """ Essa função baixa a imagem gerada pela inteligência artificial no PC. """
        name_img = f'{self.folder_img}/{name_img}'
        image = requests.get(url)
        with open(name_img, "wb") as img:
            img.write(image.content)
        self.img_save = name_img
        return self.img_save
    
    def img_blur(self, name_img:str):
        """ Essa função coloca um efeito BLUR na imagem. """
        image = Image.open(name_img)
        image = image.filter(ImageFilter.GaussianBlur(radius=10))
        self.image = image
        return self.image
    
    def color_slayer(self, size:tuple=(1024, 1024), color:tuple=(0, 0, 0, 200)):
        """ Essa função coloca uma camada com uma determinada cor sobre a imagem. """
        image = Image.new('RGBA', size, color)
        self.image = image
        return self.image

    def join_slayer(self, img1:object, img2:object):
        """ Essa função junta uma camada/imagem na outra. Geralmente pegamos uma imagem com BLUR e juntamos com a camada de cor antes criada. """
        new_img = Image.new('RGBA', img1.size, (0, 0, 0, 0))
        new_img.paste(img1, (0, 0))
        new_img.alpha_composite(img2)
        self.image = new_img
        return self.image
    
    def write_img(self, pil_img, texto, font_type:str='./auxiliary_files/BebasNeue-Regular.ttf', font_size:int=38):
        """ Essa função escreve um determinado texto na imagem. """
        font = ImageFont.truetype(font_type, font_size)
        draw = ImageDraw.Draw(pil_img)
        width, height = pil_img.size

        text = draw.textbbox((0, 0), texto, font=font)
        text_x = (width - text[2]) / 2
        text_y = (height - text[3]) / 2

        # desenhar o texto justificado na imagem
        draw.text((text_x, text_y), texto, font=font, fill=(255, 255, 255), align="center")

        self.image = pil_img
        return self.image

    def save_pil_img(self, pil_img, name_img='save.png'):
        """ Essa função salva a imagem previamente editada(POST FINAL) no seu PC. """
        pil_img.save(f'{self.folder_img}/{name_img}')
        self.img_save = name_img
        return self.img_save
