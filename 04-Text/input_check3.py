import re

while True:

    invoer = input("Voer je telefoonnummer in: ")

    patroon = r"^06-?\d{8}$"
    matches = re.findall(patroon, invoer)
    

    if(len(matches) > 0):
        break

print("Bedankt, nummer in juiste formaat:", matches[0])

while True:

    invoer = input('Voer je postcode in: ')

    patroon = r'[0-9]{4} ?[a-zA-Z]{2}'

    matches = re.findall(patroon, invoer)
    
    if(len(matches) > 0):
        break

print('Bedankt, postcode in juiste formaat:', matches[0])

while True:

    invoer = input('Voer je kenteken in: ')

    patroon = r'[A-Z]{2}-[0-9]{3}-[A-Z]{3}'

    matches = re.findall(patroon, invoer)
    
    if(len(matches) > 0):
        break

print('Bedankt, kenteken in juiste formaat:', matches[0])