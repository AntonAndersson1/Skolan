#Testar så github funkar

def karaktär():
    karaktärmeny = input("Vad heter du?")
    print(f"Väldigt bra namn valt av din mamma och pappa!")

def Insällningar(svenska, engelska, swedish, english):
    Inställningar = input("Vill du ha spelet på svenska eller engelska, Do you want the game in swedish or english")
    if svenska == True or swedish == True:
        print ("Spelet kommer vara på svenska")
        if engelska == True or english == True:
            print("The game will be on English")

        
        
    

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
        pass
    if menyval == "2":
        pass
    if menyval == "3":
        pass
    if menyval == "4":
        break