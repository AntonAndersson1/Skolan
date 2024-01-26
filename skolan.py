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
  ____________________________________________________________________________________________________
 |                                                                                                   |
 |                                                                                                   |
 |                                                                                                   |
 |     ⢧⡙⢦⡙⢦⢫⠜⣎⠵⣚⢬⢣⡓⢮⡱⡍⡞⢬⢣⠧⡹⣌⠧⡹⣌⠧⣙⠦⡹⣌⠧⡹⢌⢧⠣⡝⡜⢦⡹⢜⢆⠻⣌⠧⡹⡜⢬⢣⡝⢬⢣⠏⡼⡡⢏⡼⢌⠧⡣⢝⡬⢣⡝⢬⢓     | 
 |     ⡎⡝⢦⡹⢣⢏⠞⣬⢣⡍⣎⢧⡙⢮⡱⢥⡛⣬⢣⣍⠳⣬⠣⡗⣬⢣⡝⢮⡱⢎⡵⣩⠏⣎⢳⡹⡜⡣⡝⢮⢎⡳⢬⢳⡱⣙⠮⡱⢎⠵⣋⢞⡱⣍⠳⣜⡩⢞⡥⢫⡜⣣⠞⣥⢫     | 
 |     ⡼⣍⠶⢩⠗⡮⢜⠦⠧⡼⢰⠦⡍⢶⢩⠦⣱⢚⡴⠪⢵⢢⠧⢳⠼⡰⢎⠧⢼⡘⢦⡱⢚⡴⠣⣖⡹⠤⣝⠲⢦⠹⣆⠧⢳⡜⠦⡝⢮⠴⣋⠶⡰⢎⠗⣦⠱⡎⠶⡱⠼⢥⠺⡔⢮     | 
 |     ⠖⣜⠺⡔⡳⢼⡘⢮⠳⡼⣘⠶⡱⢎⠞⡴⢣⠞⡴⣋⢖⡣⠞⡥⢞⠴⣋⠞⡴⣊⠧⣚⢜⡲⢇⠶⣙⠖⣬⢛⡤⠻⡔⢎⡳⣜⠲⡝⣲⠲⡱⡖⡱⢎⡳⢦⢹⡒⢧⡙⢞⢆⡳⡜⠶     | 
 |     ⣙⣎⡱⢉⡝⣢⠙⣌⣣⣑⢩⢎⡅⢫⢸⡁⢏⡸⢡⡉⣎⢱⡉⣍⢪⡑⣍⡙⣨⢡⠏⣘⢬⣁⠏⣸⢩⠌⡲⢩⡐⢫⡙⣌⡱⢬⡑⣍⢥⢑⠣⣍⢱⡉⠇⣍⢲⡉⣆⢹⣈⠎⣱⢩⣉     | 
 |     ⠣⡖⣙⢢⠝⡦⢛⠴⣃⠞⡸⢆⡛⣜⠲⡅⠧⢹⠆⡳⠎⢧⠓⣎⢳⠘⡦⢛⠴⢋⡞⡱⢊⡖⡋⠶⣙⠦⡙⢧⠌⡳⠜⡤⠛⡴⠱⢎⡚⢬⠓⣎⢲⢩⠳⣜⠲⡍⠶⡹⢌⡓⢧⠳⢌     | 
 |     ⠅⡏⡜⢢⠝⡆⡙⢌⡅⢫⢘⡬⡑⢬⢓⡉⠞⣡⠚⡡⡙⢤⠉⡬⢩⠘⡅⡋⢬⠑⡥⢉⢱⠘⡱⢩⠸⢤⡉⠼⣨⠵⠉⠖⡭⢘⠅⡫⢜⢨⡙⡤⢩⢌⡓⣌⢣⠙⡒⣩⢊⡍⢦⣙⢨     | 
 |     ⢊⡕⡩⢐⣃⠞⡰⣈⢒⡃⡘⢆⡃⣒⢊⡔⢣⢘⢒⡁⣛⡰⢉⣒⢣⡘⡒⣍⢒⡉⡖⢉⣘⢚⣁⢊⡱⢒⡀⢣⣐⢪⡑⣂⡓⣪⠐⣓⡘⣐⣂⡓⣌⢢⡑⢢⢘⡁⡓⣘⡐⣂⢃⠲⣘     | 
 |     ⠄⡤⠤⢠⠄⡤⢄⠠⡄⡄⢣⠄⡄⠤⣠⠠⡄⠸⢄⡠⢄⡠⢤⠀⡤⢠⠤⡄⢤⠠⡄⣄⠠⢄⡄⡜⢠⠜⡠⠇⡸⢠⠠⠄⡤⢠⢠⠠⡄⢠⡀⣄⢠⠠⡄⠤⢠⠤⡄⡠⢤⠀⡤⢤⢀     |      
 |     ⠀⠀⡔⠀⠀⡄⠀⠐⡀⠀⢠⠀⠀⡀⢀⠀⠀⠰⠀⠀⣀⠀⠀⠄⠀⢀⠀⠄⠀⠀⡐⠀⠐⡀⠀⢀⠂⡐⠀⠀⡐⠀⠀⠀⣀⠀⠀⡂⠀⢀⠀⡀⢀⠀⠄⠐⢠⠀⠀⢄⠀⠀⣀⠀⠀            | 
 |     ⠀⠄⠤⠀⠠⠄⠀⠰⠄⠀⠠⠄⠀⠰⠀⠄⠂⠠⠄⠄⠠⠀⠄⠄⠠⠠⠄⠢⠀⠠⠔⠀⠠⠄⠠⠠⠄⠀⠤⠐⠀⠤⠀⠀⠄⠠⠀⠄⠤⠀⠀⠄⠀⠠⠆⠀⠠⠄⠀⠤⠀⠄⠤⠀⠀         |
 |     ⠀⠀⡀⠀⠀⠅⠀⠀⠀⠀⠈⠀⠄⠈⠀⠀⠈⠀⠀⠀⠈⠀⠀⠁⠠⠀⠀⠀⠈⠀⠄⠀⠈⠄⠀⠈⠀⠠⠈⠠⠀⠈⠀⠠⠁⠀⠄⠀⠀⠄⠀⠁⠀⠄⡀⠀⠌⠀⠀⡈⠀⠀⡀⢀⠀            |
 |     ⠀⠀⠀⠈⠂⠀⠉⠀⠁⠀⠈⠀⠀⠀⠈⠀⠁⠈⠀⠉⠀⠀⠁⠈⠁⠀⠀⠁⠀⠈⠀⠈⣨⡀⠀⠈⠀⠁⠈⠀⠀⠁⠀⠀⠉⠀⠀⠈⠀⠀⠈⠁⠈⠀⠁⠀⠈⠁⠀⠈⠀⠀⠀⠀⠀            |
 |     ⠀⠀⠀⠀⠄⠀⠀⠄⠀⠄⠬⠰⠤⠄⠦⠴⠒⠦⠠⠄⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠤⠬⠳⠴⠠⠆⠶⠠⠠⠈⠀⠀⠨⠀⠀⠀⠀⠤            |
 |     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠐⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣽⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                |
 |     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 |
 |     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣯⣯⣿⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            |
 |     ⣯⣿⣿⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣿⣿⣶⣷⣾⣶⣷⣾⣶⣷⣾⣶⣿⡿⠛⠻⣿⣿⣿⣶⣷⣾⣶⣷⣾⣶⣷⣾⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           |
 |     ⣿⣿⣿⣾⣿⣾⣷⢤⡀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣟⣿⣟⣿⣿⣿⣿⣿⣿⠟⠑⣿⡇⠘⠻⣿⣿⣿⣿⣟⣿⣿⣿⣿⣻⣿⣾⣇⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⢀⣀⣤⢶         |
 |     ⣛⣛⣛⣛⣛⣛⣻⣿⣿⣤⣄⡀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣏⣠⣴⢿⣟⣦⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⠀⠀⠀⢀⣾⣭⣷⣾⣷⣖⣒⣚⣓⣓⣛⣛       |
 |     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣒⢒⣀⢂⣼⠟⣿⣿⢻⣿⡟⣿⣿⡟⣻⢻⣻⢽⢸⣾⣿⣿⣿⣿⣿⣿⣿⡟⣿⡟⣿⣿⣟⢻⣻⢻⣿⢀⡐⣨⡝⣷⣿⣿⣿⣿⡉⡿⣿⣿⣿⣿⣿      |
 |     ⠟⢡⣦⠙⠻⣿⢽⣚⣿⣿⣿⣿⣿⣿⣾⣟⣾⣀⣿⣿⣸⣿⣟⣿⣿⣧⣹⣽⣼⢿⠼⠿⠿⠿⠿⣿⣿⣿⣿⣟⣿⣇⣿⣿⣇⣿⣼⢸⣿⣿⣿⣿⣾⢿⣿⣿⣿⠟⣷⠹⡿⣿⡿⢿⣿      |
 |     ⠀⣿⣿⣹⠀⣿⣿⣿⣿⣿⣿⣟⣿⣭⣯⣭⣿⠉⣭⣬⢭⣭⣭⣩⣬⣍⣿⢯⣽⢺⢼⣮⣿⣯⡾⣿⣿⣿⣿⣯⣯⡭⣨⣭⣍⢭⢭⠽⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣇⢿⢃⠸⡇      |
 |     ⢂⣼⣥⣧⠈⣿⣿⣿⣾⢿⢿⣿⣿⡟⣿⣿⢿⠀⣿⢿⢸⣿⡷⣿⣿⣧⢻⣹⢼⢫⢸⣿⣿⣿⡽⣿⣿⣿⣿⣏⣿⡇⢽⣿⣏⢾⢻⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣮⡇⣿⡇⢸⣗      |
 |     ⣷⣿⣽⣿⣿⣿⣿⣿⣷⡞⠚⣿⣯⣭⣭⣭⣿⣶⣿⣿⣾⣿⢳⣿⡟⣿⣿⣾⣿⣾⣾⣿⣿⣿⣷⣿⣿⣿⣿⣿⡟⣷⣿⣿⣷⣾⣿⣿⣾⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿      |
 |     ⠀⣂⣂⣀⠀⠀⣸⠀⢀⠚⢉⠛⡛⢛⠛⠛⠛⢛⠛⠛⠟⢛⠻⡛⠟⡛⣻⠟⣻⢻⠟⠛⠛⡛⠛⣿⡟⡛⢻⡟⠻⠛⠛⠻⠟⠟⠛⠛⢛⠛⠛⡛⠛⠛⠛⣛⣋⣃⠓⡈⠓⡀⠒⠀⣂       |
 |     ⣿⡷⣿⣛⣽⣶⣸⠀⠈⠀⠁⠀⠈⠈⠈⠉⠈⠈⠀⠁⠁⠈⠁⠉⠉⠉⠛⠛⠌⡽⠬⠌⠅⠅⠅⠼⡍⠁⠘⠋⠍⠉⠀⠉⠉⠈⠈⠈⠀⠁⢡⣞⣿⣷⣞⣱⣾⣿⣦⣔⣯⣿⣷⣾⣿       |
 |     ⣿⣿⣿⣿⣿⣿⣿⡿⠷⠶⠴⠧⠦⠶⠴⠼⠤⠦⠧⠶⠶⠴⠥⠦⠦⠮⠶⠶⢽⠁⠁⠁⠁⠁⠀⠁⢳⠮⠶⠼⠦⠶⠴⠴⠤⠦⠶⠶⠵⡴⠿⠿⠿⠿⠿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿      |
 |     ⣿⣷⣿⣾⣶⣯⣷⣶⣶⣶⣶⣷⡽⣾⣇⣀⣀⣠⣀⣀⣀⣠⣀⣄⣀⣠⣀⣀⣞⣀⣄⡂⡄⣄⣠⣀⢚⣄⣀⣀⣀⣠⣀⣀⣄⣠⢀⣀⣰⣻⣿⣷⣿⣿⣇⣠⣸⣮⣷⣾⣿⣾⣿⣿⣿      |
 |     ⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣽⣽⡿⠄⠆⠄⠆⠄⠆⠔⠰⠰⢹⣾⣧⣿⣿⣾⣷⣿⣿⣾⣾⣿⣽⣯⣿⣽⣿⣿⣿⣿⣿⣿⣿⣽⣿⡿⣽⣿      |
 |     ⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣯⣭⢭⠭⡍⣭⠉⣍⢉⣉⢉⡉⣉⣉⠩⣉⣽⡡⡨⡠⣁⡁⣅⣀⢄⣁⣄⢅⣯⣍⣉⠍⣉⠉⣍⠉⣉⡉⣉⢉⢍⢉⣉⠩⣉⢉⢩⢉⡉⢩⣩⣭⣼⣻⣿      |
 |     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⠧⠠⠡⠡⠠⠨⠤⠌⠌⠄⠌⠌⠤⢿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      |
 |     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢑⣣⣟⣞⣸⢸⣛⡖⡇⣧⣳⣹⡒⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      |
 |                                                                                                    |
 |                          Skolan av Anton Andersson & Johan Ahl                                     |
 |                                                                                                    |
 |                                                                                                    |
 |____________________________________________________________________________________________________|   
 
        """)
exit = ("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣤⣼⣿⣿⣿⣿⣿⣿⣷⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣢⣾⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡟⠛⢻⠉⡉⠍⠁⠁⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠏⢠⢀⡼⡄⠃⠤⠀⠀⠀⠀⠀⡐⠸⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢰⣸⡎⣀⣷⣤⣶⣶⣶⣦⡀⠀⠈⠓⢿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣇⣤⣯⣿⣿⣿⣿⣿⣿⣿⣭⣯⡆⠀⠀⠘⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣻⣿⣿⣼⠀⢹⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⢘⣿⠙⠡⢽⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣛⣿⣯⠏⠀⢀⣿⣿⣿⣯⣠⡀⠀⠀⠀⢀⣾⡏⠒⢻⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡟⢘⣏⣺⣤⣬⣭⣼⣿⣿⣯⡉⢻⣦⣌⣦⣾⣿⣿⡚⠾⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢹⡼⣿⣿⢼⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡿⣿⢿⡟⢳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣿⣧⡞⣻⣩⣽⡽⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⣇⣬⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡿⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡛⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡃⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⡟⠻⢿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣍⠓⠲⠤⢤⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠈⣿⡏⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠈⢯⡁⠀⠀⠀⠉⠹⠶⢤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⢀⠹⣿⡆⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⣤⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⢩⠀⢸⡄⢹⣿⣦⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣤⡄⠀⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠋⡀⣀⣰⣿⠀⠄⠹⣾⣿⣿⡿⣿⠀⢠⣤⣀⣴⣤⣤⡴⠶⠶⠿⠿⠛⠛⠋⠉⠉⣠⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⢀⡱⠏⠉⡟⠃⠀⠀⠀⢸⣿⣿⠇⣿⡴⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⢋⣡⣶⣿⣂⡼⠁⠉⠙⠋⠙⠿⠟⣢⣄⢿⡟⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠈⠀⠀
⠀⠀⠀⢀⣠⠴⠚⠉⠉⠀⠀⠀⠀⠀⣸⡿⠟⠀⠀⠀⠀⠀⠀⠲⣾⡛⣿⣬⡄⠀⠀⠁⠠⣤⠆⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⡟⣿⡟⠀⠀⠂⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀
⠞⠁⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⡀⡀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠁⠆⠀⠀⠀


Du lyckade rymma från skolan 

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
    
    print("Du har gått igenom dörren och befinner dig nu i skolans gamla bibliotek. Det är ett rum fyllt med tidens viskningar, bokhyllor sträcker sig från golv till tak, och de många böckerna bär på berättelser från en svunnen tid. Rummet badar i ett dammigt halvmörker, och den enda ljudet är dina egna steg på det knarrande trägolvet. En bok har fallit ned på golvet, dess sidor fladdrar svagt i draget.")
    print("Medan du vandrar mellan hyllorna, upptäcker du att biblioteket leder vidare till tre nya dörrar. Varje dörr ser annorlunda ut, den första är robust och ser ut att vara gjord av ek, den andra är delvis glasad och du kan skymta en dunkelt upplyst korridor bakom, och den tredje är enkel och oansenlig, nästan lätt att missa. Du stannar upp och betraktar dem. Vilken dörr ska du välja att gå igenom? Kanske håller svaren du söker på att dölja sig bakom en av dem.")
    if not valj_dorr(3):
        print(f"{Dead}")
        return
    
    print("Efter att ha utforskat bibliotekets dammiga gångar och hemligheter, finner du dig själv tillbaka vid utgången. Du står nu i en smal korridor, som sträcker sig bort från bibliotekets trygga tystnad. Här känns luften tyngre, fylld av en obehaglig förväntan. Längre fram delar korridoren sig i två, och du måste välja din fortsatta väg.")
    print("Till höger ser korridoren ut att leda till ett område med blekt ljus som sipprar in genom sprickor i väggarna, och du kan höra ett svagt, nästan hypnotiskt, brus. Till vänster breder mörkret ut sig, och korridoren verkar slingra sig iväg mot något okänt, med en aura av tystnad och hemlighetsfullhet. Din hand vilar på den kalla väggen för stöd, och du funderar över vilken riktning som är säkrast, eller kanske mest riskfylld. Ska du gå till höger och utforska ljuset, eller till vänster där mörkret kallar?")
    riktning = input("Vill du gå till höger eller vänster? (höger/vänster) ")
    print("Du tar ett djupt andetag och styr dina steg åt vänster, in i korridorens mörkare del. Här är luften kallare och varje steg känns tyngre. Mörkret omsluter dig snart helt och du måste famla dig fram längs väggarna för att inte snubbla. Den tysta korridoren tycks sträcka sig oändligt, men till slut öppnar den sig till en större sal. I mörkret kan du urskilja konturerna av något stort i rummets mitt, något som verkar vänta på att upptäckas. En känsla av något oupptäckt, kanske farligt, hänger i luften.")
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
    print("När du svänger till höger, möts du av en korridor som badar i ett svagt, fläckvis ljus. Ljuset verkar komma från små glipor i taket, och du kan skönja dammpartiklar som dansar i strimmorna. Korridoren är smalare här, och väggarna känns nästan som om de närmar sig. Dina steg ekar tyst när du fortsätter framåt. Efter en stund leder korridoren till en liten dörr, halvt dold av en hängande ljuskrona. Bakom dörren hör du svaga, nästan otydliga, ljud – som om någon eller något rör sig därinne.")
    if not valj_dorr(2):
        print(f"{Dead}")
        return
    
    print("Du befinner dig nu framför fyra dörrar, var och en unik i sitt slag och omgivna av en myriad av föremål som strösslar korridoren. Dessa ting verkar ha sina egna berättelser, övergivna och glömda i tiden. Framför dig öppnar sig möjligheterna: Ska du söka skydd bland dessa gömda reliker och gömma dig från det okända, eller har du modet att stiga igenom en av dessa dörrar? Valet ligger i dina händer, en chans att fortsätta utforska de djupare hemligheterna som väntar, eller en stund av försiktig eftertanke i skuggorna av det förflutna.")
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