# Kärmespeli
# Soveltava projekti 2020
# Johanna Seulu, Juhana Kuparinen, Juho Ollila

VERSION = 0.6

'''
Versiosta 0.6 eteenpäin, kaikki käyttämämme luokat sijaitsevat game_modules -kansiossa omissa moduuleissaan
(lukuunottamatta Menu ja Game luokkia, jotka ovat game_engine.py moduulissa). Tästä eteenpäin myös uudet tekemämme
luokat olisi hyvä tehdä omiin moduuleihinsa (eli omaan .py tiedostoon) game_modules kansiossa.
'''

from game_modules.game_engine import Menu

def main():
    print("Running on version: " + str(VERSION))
    menu = Menu()
    menu.main_menu()

if __name__ == "__main__":
    main()

