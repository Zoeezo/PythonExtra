from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open('./meme assets/meme_background.png')
lettertype = ImageFont.truetype('./meme assets/impact.ttf', 30)

breedte = achtergrond.width
hoogte = achtergrond.height

tekengebied = ImageDraw.Draw(achtergrond)

tekst = "Penguin be vibin' but centered and white!"

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2  


tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))

achtergrond.show()

achtergrond.save('./meme_met_tekst3.png')
