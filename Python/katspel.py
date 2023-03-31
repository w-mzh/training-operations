from playsound import playsound
import random
import os
import time

clear = lambda: os.system('cls') #on Windows System


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

aantal_dozen = 50
toegestane_doosnummers = list(range(1,aantal_dozen+1))
aantal_pogingen = 0
cheatmode = True



# Plaats de kat in een willekeurige doos
kat_positie = random.randint(1, aantal_dozen+1)

# Spelbord
dozen = ["[]", "[]", "[]", "[]", "[]"]


# Game loop
while True:
    clear()
    print('''
  
  
  
  
  __________
 /         /|
+---------+ |
|         | |
|         | /
+---------+/
''')

    if cheatmode == True:
        print(bcolors.HEADER, "Cheat mode: De kat zit in doos", kat_positie, bcolors.ENDC)

    #Vraag gebruiker om een doosnummer
    doos_nummer = int(input("Kies een doosnummer van 1 t/m " + str(aantal_dozen) + ":"  ))
    clear() 

    if doos_nummer == 0:
        print("Doei")
        break  
    if doos_nummer not in toegestane_doosnummers:
        print(bcolors.FAIL, "Vul een nummer in tussen 1-",aantal_dozen, bcolors.ENDC)
        continue
         
    aantal_pogingen += 1

    print(bcolors.OKBLUE, "Aantal pogingen:", aantal_pogingen, bcolors.ENDC)

    # Kijk of de kat in de gekozen doos zit
    if doos_nummer == kat_positie:
        clear()
        print('''
   _________
  | |\_._/| |
  | | o o | |
  | (  T  ) |
  |.^`-^-'^.|
 /         /|
+---------+ |
|         | |
|         | /
+---------+/
''')
        print(bcolors.OKGREEN, "Gefeliciteerd! Je hebt de kat gevonden.", bcolors.ENDC)
        print(bcolors.OKCYAN, "Je had",aantal_pogingen , "pogingen nodig om de kat te vinden.", bcolors.ENDC)    
        print("\n")
        playsound("smellycat.mp3")
        break
    else:
        clear()
        print('''
   _________
  |         |
  |         |
  |         |
  |_________|
 /         /|
+---------+ |
|         | |
|         | /
+---------+/
''')
        print(bcolors.OKCYAN, "Haha, hier zit de kat niet!", bcolors.ENDC)
        time.sleep(2)

    # Verplaats de kat
    if kat_positie == 1:
        kat_positie += 1
    elif kat_positie == aantal_dozen:
        kat_positie -= 1
    else:
        kat_positie += random.choice([-1, 1])

    # Update het spelbord
    dozen = ["[]" if i != kat_positie - 1 else "[Kat]" for i in range(aantal_dozen)]
    print("  ".join(dozen))