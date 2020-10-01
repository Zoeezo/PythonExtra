bestand = open("klasgenoten.txt", "r")

tekst_regel = bestand.readline().strip()


while tekst_regel:
    print(tekst_regel)

    tekst_regel = bestand.readline().strip()