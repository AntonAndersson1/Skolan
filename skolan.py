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
    print(f"Valdigt bra namn valt av din mamma och pappa!")

def Insallningar(svenska, engelska, swedish, english):
    Installningar = input("Vill du ha spelet pa svenska eller engelska, Do you want the game in swedish or english")
    if svenska == True or swedish == True:
        print(f"Spelet kommer vara pa svenska")
        if engelska == True or english == True:
            print(f"The game will be on English")

def Spel():
    vald_dorr = int(input("Vilken dorr vill du gå igenom (1, 2 eller 3)? "))

    farlig_dorr = random.randint(1, 3)

    if vald_dorr == farlig_dorr:
        print(f"{Dead}")
    else:
        print("du overlever och kommer till nasta rum.")
        
        
    

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