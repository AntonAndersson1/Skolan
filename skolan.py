#Testar så github funkar
import random

def karaktär():
    karaktärmeny = input("Vad heter du?")
    print(f"Väldigt bra namn valt av din mamma och pappa!")

def Insällningar(svenska, engelska, swedish, english):
    Inställningar = input("Vill du ha spelet på svenska eller engelska, Do you want the game in swedish or english")
    if svenska == True or swedish == True:
        print ("Spelet kommer vara på svenska")
        if engelska == True or english == True:
            print("The game will be on English")

def Spel():
    vald_dörr = int(input("Vilken dörr vill du gå igenom (1, 2 eller 3)? "))

    farlig_dörr = random.randint(1, 3)

    if vald_dörr == farlig_dörr:
        print("du överlever och kommer till nästa par var dörrar.")
    else:
        print("gg")
        
    

while True:
    menyval = input(
        """
1. Starta Spelet

2. Karaktär Meny

3. Inställningar

4. Avaluta Spelet
        """
    )

    if menyval == "1":
        Spel()
    if menyval == "2":
        karaktär()
    if menyval == "3":
        Insällningar()
    if menyval == "4":
        break