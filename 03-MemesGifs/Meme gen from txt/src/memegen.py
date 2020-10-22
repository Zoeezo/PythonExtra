from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from os import mkdir

lettertype = ImageFont.truetype('../assets/impact.ttf', 40)
bestand = open('./input/strings.txt')


outputmap = datetime.now().strftime('%d_%m_%Y_%H%M%S')
mkdir('./output/' + outputmap)


tekstRegel = bestand.readline().strip()
x = 1
while tekstRegel:
    achtergrond = Image.open('../assets/meme_background.png')

    tekengebied = ImageDraw.Draw(achtergrond)

    tekstBreedte, tekstHoogte = tekengebied.textsize(tekstRegel, font=lettertype)

    tekstX = (achtergrond.width - tekstBreedte) / 2
    tekstY = (achtergrond.height - tekstHoogte) / 2

    tekengebied.multiline_text((tekstX-2, tekstY-2), tekstRegel, font=lettertype, fill=(255,255,255))

    achtergrond.save('./output/' + outputmap + '/' + str(x) + '.png')
    x += 1
    tekstRegel = bestand.readline().strip()
