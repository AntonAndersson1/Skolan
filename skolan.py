#Testar så github funkar
import random

fortsatt = ("{menyval}")

Dead = ("""
        ⠀⢀⣠⣤⣶⣶⣾⣿⣿⣷⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠛⠉⠉⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣶⣄⠀⠀⠀
⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄⠀⠀⠀⠀⠙⢿⣿⣧⠀⠀
⠀⣰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣶⣾⣿⣧⣄⠀⠀⠀⠀⠀⠹⣿⣷⠀
⢠⡿⠀⠀⠀⠀⡀⣠⡤⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠛⠉⠀⠀⠀⠀⠀⠀⢹⣿⡇
⣼⡇⠀⠀⠀⣼⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
⣿⡇⠀⠀⣰⠟⢿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿
⣿⣷⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⣸⡏
⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⠿⠿⠿⣿⣿⣿⠇⠀⠀⠀⢠⡿⠀
⠈⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⠀
⠀⠘⣿⣿⣦⡀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀
⠀⠀⠈⠻⣿⣿⣷⣄⡀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠿⣿⣿⣷⣦⣤⣄⣀⣀⣀⣀⣀⣤⣴⣾⠿⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⣿⣿⣿⠿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")


def valj_dorr(antal_dorrar):
    """Låter spelaren välja en dörr och avgör om det var den säkra dörren."""
    farlig_dorr = random.randint(1, antal_dorrar)
    vald_dorr = int(input(f"Vilken dörr vill du gå igenom (1-{antal_dorrar})? "))
    return vald_dorr != farlig_dorr

#Funktion för karaktären ska kunna ha ett namn
def karaktar():
    karaktarmeny = input("Vad heter du?")
    print(f"Valdigt bra namn valt av din mamma och pappa!")

#Funktion för att inställningar ska kunna fungera
def Insallningar(svenska, engelska, swedish, english):
    Installningar = input("Vill du ha spelet pa svenska eller engelska, Do you want the game in swedish or english")
    if svenska == True or swedish == True:
        print(f"Spelet kommer vara pa svenska")
    if engelska == True or english == True:
        print(f"The game will be on English")
    else: print("Someting went wrong.(Något gick fel.)")

#Funktion för att spelet ska start
def Spel():
    print("Start")
    if not valj_dorr(3):
        print(f"{Dead}")
        return
    
    if not valj_dorr(3):
        print(f"{Dead}")
        return
    
    riktning = input("Vill du gå till höger eller vänster? (höger/vänster) ")
    if riktning.lower() == "vänster":
        print(f"Felaktigt val. {Dead}")
        return
    elif riktning.lower() != "höger":
        print(f"{Dead}.")
        return
    
    val = input("Vill du gömma dig (1) eller välja en dörr (2-5)? ")
    if val == "1" or not valj_dorr(5):
        print(f"{Dead}")
        return
    
    print("EXIT, du överlevde!")
        


#Startmeny vi använden if-sats för att kunna se vad spelar vill göra.
while True:
    menyval = input(
        """
1. Starta Spelet

2. Karaktar Meny

3. Installningar

4. Avsluta Spelet
        """
    )

    if menyval == "1":
        Spel()
    if menyval == "2":
        karaktar()
    if menyval == "3":
        Insallningar()
    if menyval == "4":
        break