import re

while True:

    invoer = input("Voer je telefoonnummer in: ")

    patroon = r"^06-?\d{8}$"
    matches = re.findall(patroon, invoer)
    

    if(len(matches) > 0):
        break

print("Bedankt, nummer in juiste formaat:", matches[0])

