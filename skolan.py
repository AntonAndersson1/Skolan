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
Starting = ("""
⢧⡙⢦⡙⢦⢫⠜⣎⠵⣚⢬⢣⡓⢮⡱⡍⡞⢬⢣⠧⡹⣌⠧⡹⣌⠧⣙⠦⡹⣌⠧⡹⢌⢧⠣⡝⡜⢦⡹⢜⢆⠻⣌⠧⡹⡜⢬⢣⡝⢬⢣⠏⡼⡡⢏⡼⢌⠧⡣⢝⡬⢣⡝⢬⢓
⡎⡝⢦⡹⢣⢏⠞⣬⢣⡍⣎⢧⡙⢮⡱⢥⡛⣬⢣⣍⠳⣬⠣⡗⣬⢣⡝⢮⡱⢎⡵⣩⠏⣎⢳⡹⡜⡣⡝⢮⢎⡳⢬⢳⡱⣙⠮⡱⢎⠵⣋⢞⡱⣍⠳⣜⡩⢞⡥⢫⡜⣣⠞⣥⢫
⡼⣍⠶⢩⠗⡮⢜⠦⠧⡼⢰⠦⡍⢶⢩⠦⣱⢚⡴⠪⢵⢢⠧⢳⠼⡰⢎⠧⢼⡘⢦⡱⢚⡴⠣⣖⡹⠤⣝⠲⢦⠹⣆⠧⢳⡜⠦⡝⢮⠴⣋⠶⡰⢎⠗⣦⠱⡎⠶⡱⠼⢥⠺⡔⢮
⠖⣜⠺⡔⡳⢼⡘⢮⠳⡼⣘⠶⡱⢎⠞⡴⢣⠞⡴⣋⢖⡣⠞⡥⢞⠴⣋⠞⡴⣊⠧⣚⢜⡲⢇⠶⣙⠖⣬⢛⡤⠻⡔⢎⡳⣜⠲⡝⣲⠲⡱⡖⡱⢎⡳⢦⢹⡒⢧⡙⢞⢆⡳⡜⠶
⣙⣎⡱⢉⡝⣢⠙⣌⣣⣑⢩⢎⡅⢫⢸⡁⢏⡸⢡⡉⣎⢱⡉⣍⢪⡑⣍⡙⣨⢡⠏⣘⢬⣁⠏⣸⢩⠌⡲⢩⡐⢫⡙⣌⡱⢬⡑⣍⢥⢑⠣⣍⢱⡉⠇⣍⢲⡉⣆⢹⣈⠎⣱⢩⣉
⠣⡖⣙⢢⠝⡦⢛⠴⣃⠞⡸⢆⡛⣜⠲⡅⠧⢹⠆⡳⠎⢧⠓⣎⢳⠘⡦⢛⠴⢋⡞⡱⢊⡖⡋⠶⣙⠦⡙⢧⠌⡳⠜⡤⠛⡴⠱⢎⡚⢬⠓⣎⢲⢩⠳⣜⠲⡍⠶⡹⢌⡓⢧⠳⢌
⠅⡏⡜⢢⠝⡆⡙⢌⡅⢫⢘⡬⡑⢬⢓⡉⠞⣡⠚⡡⡙⢤⠉⡬⢩⠘⡅⡋⢬⠑⡥⢉⢱⠘⡱⢩⠸⢤⡉⠼⣨⠵⠉⠖⡭⢘⠅⡫⢜⢨⡙⡤⢩⢌⡓⣌⢣⠙⡒⣩⢊⡍⢦⣙⢨
⢊⡕⡩⢐⣃⠞⡰⣈⢒⡃⡘⢆⡃⣒⢊⡔⢣⢘⢒⡁⣛⡰⢉⣒⢣⡘⡒⣍⢒⡉⡖⢉⣘⢚⣁⢊⡱⢒⡀⢣⣐⢪⡑⣂⡓⣪⠐⣓⡘⣐⣂⡓⣌⢢⡑⢢⢘⡁⡓⣘⡐⣂⢃⠲⣘
⠄⡤⠤⢠⠄⡤⢄⠠⡄⡄⢣⠄⡄⠤⣠⠠⡄⠸⢄⡠⢄⡠⢤⠀⡤⢠⠤⡄⢤⠠⡄⣄⠠⢄⡄⡜⢠⠜⡠⠇⡸⢠⠠⠄⡤⢠⢠⠠⡄⢠⡀⣄⢠⠠⡄⠤⢠⠤⡄⡠⢤⠀⡤⢤⢀
⠀⠀⡔⠀⠀⡄⠀⠐⡀⠀⢠⠀⠀⡀⢀⠀⠀⠰⠀⠀⣀⠀⠀⠄⠀⢀⠀⠄⠀⠀⡐⠀⠐⡀⠀⢀⠂⡐⠀⠀⡐⠀⠀⠀⣀⠀⠀⡂⠀⢀⠀⡀⢀⠀⠄⠐⢠⠀⠀⢄⠀⠀⣀⠀⠀
⠀⠄⠤⠀⠠⠄⠀⠰⠄⠀⠠⠄⠀⠰⠀⠄⠂⠠⠄⠄⠠⠀⠄⠄⠠⠠⠄⠢⠀⠠⠔⠀⠠⠄⠠⠠⠄⠀⠤⠐⠀⠤⠀⠀⠄⠠⠀⠄⠤⠀⠀⠄⠀⠠⠆⠀⠠⠄⠀⠤⠀⠄⠤⠀⠀
⠀⠀⡀⠀⠀⠅⠀⠀⠀⠀⠈⠀⠄⠈⠀⠀⠈⠀⠀⠀⠈⠀⠀⠁⠠⠀⠀⠀⠈⠀⠄⠀⠈⠄⠀⠈⠀⠠⠈⠠⠀⠈⠀⠠⠁⠀⠄⠀⠀⠄⠀⠁⠀⠄⡀⠀⠌⠀⠀⡈⠀⠀⡀⢀⠀
⠀⠀⠀⠈⠂⠀⠉⠀⠁⠀⠈⠀⠀⠀⠈⠀⠁⠈⠀⠉⠀⠀⠁⠈⠁⠀⠀⠁⠀⠈⠀⠈⣨⡀⠀⠈⠀⠁⠈⠀⠀⠁⠀⠀⠉⠀⠀⠈⠀⠀⠈⠁⠈⠀⠁⠀⠈⠁⠀⠈⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠄⠀⠀⠄⠀⠄⠬⠰⠤⠄⠦⠴⠒⠦⠠⠄⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠤⠬⠳⠴⠠⠆⠶⠠⠠⠈⠀⠀⠨⠀⠀⠀⠀⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠐⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣽⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣯⣯⣿⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣯⣿⣿⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣿⣿⣶⣷⣾⣶⣷⣾⣶⣷⣾⣶⣿⡿⠛⠻⣿⣿⣿⣶⣷⣾⣶⣷⣾⣶⣷⣾⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣾⣿⣾⣷⢤⡀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣟⣿⣟⣿⣿⣿⣿⣿⣿⠟⠑⣿⡇⠘⠻⣿⣿⣿⣿⣟⣿⣿⣿⣿⣻⣿⣾⣇⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⢀⣀⣤⢶
⣛⣛⣛⣛⣛⣛⣻⣿⣿⣤⣄⡀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣏⣠⣴⢿⣟⣦⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⠀⠀⠀⢀⣾⣭⣷⣾⣷⣖⣒⣚⣓⣓⣛⣛
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣒⢒⣀⢂⣼⠟⣿⣿⢻⣿⡟⣿⣿⡟⣻⢻⣻⢽⢸⣾⣿⣿⣿⣿⣿⣿⣿⡟⣿⡟⣿⣿⣟⢻⣻⢻⣿⢀⡐⣨⡝⣷⣿⣿⣿⣿⡉⡿⣿⣿⣿⣿⣿
⠟⢡⣦⠙⠻⣿⢽⣚⣿⣿⣿⣿⣿⣿⣾⣟⣾⣀⣿⣿⣸⣿⣟⣿⣿⣧⣹⣽⣼⢿⠼⠿⠿⠿⠿⣿⣿⣿⣿⣟⣿⣇⣿⣿⣇⣿⣼⢸⣿⣿⣿⣿⣾⢿⣿⣿⣿⠟⣷⠹⡿⣿⡿⢿⣿
⠀⣿⣿⣹⠀⣿⣿⣿⣿⣿⣿⣟⣿⣭⣯⣭⣿⠉⣭⣬⢭⣭⣭⣩⣬⣍⣿⢯⣽⢺⢼⣮⣿⣯⡾⣿⣿⣿⣿⣯⣯⡭⣨⣭⣍⢭⢭⠽⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣇⢿⢃⠸⡇
⢂⣼⣥⣧⠈⣿⣿⣿⣾⢿⢿⣿⣿⡟⣿⣿⢿⠀⣿⢿⢸⣿⡷⣿⣿⣧⢻⣹⢼⢫⢸⣿⣿⣿⡽⣿⣿⣿⣿⣏⣿⡇⢽⣿⣏⢾⢻⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣮⡇⣿⡇⢸⣗
⣷⣿⣽⣿⣿⣿⣿⣿⣷⡞⠚⣿⣯⣭⣭⣭⣿⣶⣿⣿⣾⣿⢳⣿⡟⣿⣿⣾⣿⣾⣾⣿⣿⣿⣷⣿⣿⣿⣿⣿⡟⣷⣿⣿⣷⣾⣿⣿⣾⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿
⠀⣂⣂⣀⠀⠀⣸⠀⢀⠚⢉⠛⡛⢛⠛⠛⠛⢛⠛⠛⠟⢛⠻⡛⠟⡛⣻⠟⣻⢻⠟⠛⠛⡛⠛⣿⡟⡛⢻⡟⠻⠛⠛⠻⠟⠟⠛⠛⢛⠛⠛⡛⠛⠛⠛⣛⣋⣃⠓⡈⠓⡀⠒⠀⣂
⣿⡷⣿⣛⣽⣶⣸⠀⠈⠀⠁⠀⠈⠈⠈⠉⠈⠈⠀⠁⠁⠈⠁⠉⠉⠉⠛⠛⠌⡽⠬⠌⠅⠅⠅⠼⡍⠁⠘⠋⠍⠉⠀⠉⠉⠈⠈⠈⠀⠁⢡⣞⣿⣷⣞⣱⣾⣿⣦⣔⣯⣿⣷⣾⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠷⠶⠴⠧⠦⠶⠴⠼⠤⠦⠧⠶⠶⠴⠥⠦⠦⠮⠶⠶⢽⠁⠁⠁⠁⠁⠀⠁⢳⠮⠶⠼⠦⠶⠴⠴⠤⠦⠶⠶⠵⡴⠿⠿⠿⠿⠿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣿⣾⣶⣯⣷⣶⣶⣶⣶⣷⡽⣾⣇⣀⣀⣠⣀⣀⣀⣠⣀⣄⣀⣠⣀⣀⣞⣀⣄⡂⡄⣄⣠⣀⢚⣄⣀⣀⣀⣠⣀⣀⣄⣠⢀⣀⣰⣻⣿⣷⣿⣿⣇⣠⣸⣮⣷⣾⣿⣾⣿⣿⣿
⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣽⣽⡿⠄⠆⠄⠆⠄⠆⠔⠰⠰⢹⣾⣧⣿⣿⣾⣷⣿⣿⣾⣾⣿⣽⣯⣿⣽⣿⣿⣿⣿⣿⣿⣿⣽⣿⡿⣽⣿
⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣯⣭⢭⠭⡍⣭⠉⣍⢉⣉⢉⡉⣉⣉⠩⣉⣽⡡⡨⡠⣁⡁⣅⣀⢄⣁⣄⢅⣯⣍⣉⠍⣉⠉⣍⠉⣉⡉⣉⢉⢍⢉⣉⠩⣉⢉⢩⢉⡉⢩⣩⣭⣼⣻⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⠧⠠⠡⠡⠠⠨⠤⠌⠌⠄⠌⠌⠤⢿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢑⣣⣟⣞⣸⢸⣛⡖⡇⣧⣳⣹⡒⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")
#Funktion för dörrarna som gör så att spelet har en mening
def valj_dorr(antal_dorrar):
    """Låter spelaren välja en dörr och avgör om det var den säkra dörren."""
    farlig_dorr = random.randint(1, antal_dorrar)
    vald_dorr = int(input(f"Vilken dörr vill du gå igenom (1-{antal_dorrar})? "))
    return vald_dorr != farlig_dorr

#Funktion för karaktären ska kunna ha ett namn
def karaktar():
    karaktarmeny = input("Vad heter du?")
    print(f"Valdigt bra namn valt av din mamma och pappa!")
    namn = karaktar

#Funktion för att spelguiden ska fungera så att du får upp en guide hur spelet funkar.
def Spelguide():
    Spelguide = input("Detta spel går ut på att du ska överleva en mördare i en skola. Du kommer få olika valmöjligheter om vad du vill göra för att välja valmöjlighet så skriver du den siffran på det valet du vill välja. Ibland kommer du få ett val som säger vill du gömma dig eller gå vidare då skriver du 1 ifall du vill gömma dig och 3 ifall du vill fortsätta framåt. Ditt mål med spelet är att du ska överleva och lyckas rymma skolan med någon av de olika exitsen som finns. När du har läst klart allt och är redo att spela kan du skriva meny för att komma till menyn.   ")

    

#Funktion för att spelet ska start
def Spel():
    print("Du står framför den gamla, slitna skolbyggnaden, dess väggar är täckta av mossa och fönstren ser ut som tomma ögonhålor. Det är en kylig och dimmig morgon, och du kan knappt urskilja toppen av skolan genom dimman. Med ett djupt andetag tar du tag i det kalla dörrhandtaget och skjuter upp den tunga träporten.")
    print("Dörren faller igen bakom dig med ett ödesmättat slammer. Du rycker i handtaget, men det är förgäves dörren är låst. Ett kallt rysningar löper längs din ryggrad när du inser att du är fast.")
    print("Du vandrar genom de dunkla korridorerna, där varje steg ekar genom tystnaden. Gamla affischer fladdrar i draget och skuggorna verkar röra sig i ögonvrån. Framför dig finns flera dörrar, var och en ser lika inbjudande ut som den är skrämmande")
    print("Du stannar upp framför en rad av dörrar. Varje dörr har sin egen mystiska karaktär - en ser robust och tung ut, en annan är mjukt insvept i skuggor, och en tredje är halvöppen, med ett svagt ljus som sipprar ut. Vilken dörr väljer du?")

    if not valj_dorr(3): 
        print(f"{Dead}")
        return
    
    if not valj_dorr(3):
        print(f"{Dead}")
        return
    
    
    riktning = input("Vill du gå till höger eller vänster? (höger/vänster) ")
    if riktning.lower() == "vänster":
        if not valj_dorr(2):
            print(f"{Dead}")
            return
        else:
            print(f"Det är en Deadend. Spelet är över{Dead}.")
            return
    elif riktning.lower() != "höger":
        print(f"Felaktigt val. Spelet är över {Dead}.")
        return
    
    if not valj_dorr(2):
        print(f"{Dead}")
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

3. Spelguide

4. Avsluta Spelet
        """
    )

    if menyval == "1":
        Spel()
    if menyval == "2":
        karaktar()
    if menyval == "3":
        Spelguide()
    if menyval == "4":
        break