from PIL import Image

afbeelding = Image.open('./penguin.jpg')

breedte = afbeelding.width
hoogte = afbeelding.height

helft_breedte = breedte // 2
helf_hoogte = hoogte // 2

nieuwe_afmeting = (helft_breedte, helf_hoogte)

kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

kleinere_afbeelding.save('./penguin_klein.png')
kleinere_afbeelding.show()