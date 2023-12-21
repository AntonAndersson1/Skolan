#Testar så github funkar
import random

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




def karaktar():
    karaktarmeny = input("Vad heter du?")
    print(f"Väldigt bra namn valt av din mamma och pappa!")

def Insallningar(svenska, engelska, swedish, english):
    Installningar = input("Vill du ha spelet på svenska eller engelska, Do you want the game in swedish or english")
    if svenska == True or swedish == True:
        print ("Spelet kommer vara på svenska")
        if engelska == True or english == True:
            print("The game will be on English")

def Spel():
    vald_dorr = int(input("Vilken dörr vill du gå igenom (1, 2 eller 3)? "))

    farlig_dorr = random.randint(1, 3)

    if vald_dorr == farlig_dorr:
        print("du överlever och kommer till nästa par var dörrar.")
    else:
        print(f"{Dead}")
        
        
    

while True:
    menyval = input(
        """
1. Starta Spelet

2. Karaktar Meny

3. Installningar

4. Avaluta Spelet
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