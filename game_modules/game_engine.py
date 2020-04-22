import pygame, sys
import math
import random
from enum import Enum
from typing import Tuple
from pygame.locals import *
from game_modules.Snake import Snake
from game_modules.Apple import Apple
from game_modules.Obstacle import Obstacle


class Menu:
    # Kun peli käynnistetään, tällä enum -luokalla tiedetään
    # mikä vaikeustaso on.
    class Difficulties(Enum):
        Easy = 0
        Normal = 1
        Hard = 2

    # Kun peli käynnistetään, tällä enum -luokalla tiedetään
    # mikä vaikeustaso on.
    class Gamemodes(Enum):
        Solo = 1
        Duel = 2

    menuWidth = 800
    menuHeight = 600
    menuResolution = (menuWidth, menuHeight)
    clock = pygame.time.Clock()
    menu_screen = pygame.display.set_mode(menuResolution)

    black = (10, 10, 10)
    white = (255, 255, 255)
    green = (150, 185, 150)
    light_green = (150, 255, 150)
    red = (185, 150, 150)
    light_red = (255, 150, 150)
    gray = (150, 150, 150)
    light_gray = (200, 200, 200)
    light_yellow = (255, 255, 102)
    yellow = (255, 255, 204)

    def __init__(self):
        self.running = True

    def text_object(self, text, font, colour):
        textSurface = font.render(text, True, colour)
        return textSurface, textSurface.get_rect()

    # ic = inactive colour eli väri joka on käytössä kun hiiri ei ole napin päällä
    # ac = active colour eli väri joka tulee käyttöön kun hiirellä mennään napin päälle
    def button(self, message, x, y, width, height, ic, ac, action=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Näppäimen luominen
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.menu_screen, ac, (x, y, width, height))

            if click[0] == 1 and action != None:
                # Päävalikon toiminnot
                if action == "play":
                    self.level_select()
                elif action == "quit":
                    pygame.quit()
                    quit()
                elif action == "credits":
                    self.credits()
                # Tason valintavalikon toiminnot
                elif action == "easy":
                    Peli = Game(self.Difficulties.Easy, self.Gamemodes.Solo)
                    Peli.start_game(400, 400)
                elif action == "normal":
                    Peli = Game(self.Difficulties.Normal, self.Gamemodes.Duel)
                    Peli.start_game(600, 600)
                elif action == "hard":
                    Peli = Game(self.Difficulties.Hard, self.Gamemodes.Solo)
                    Peli.start_game(800, 600)


        else:
            pygame.draw.rect(self.menu_screen, ic, (x, y, width, height))

        # Teksti
        textCont = pygame.font.Font('OpenSans-Regular.ttf', 40)
        textSurf, textRect = self.text_object(message, textCont, self.black)
        textRect.center = (math.floor((self.menuWidth / 2)), y + 35)
        self.menu_screen.blit(textSurf, textRect)

    # Aloitus valikko pelille
    def main_menu(self):

        self.menuWidth = 800
        self.menuHeight = 600
        self.menuResolution = (self.menuWidth, self.menuHeight)
        self.menu_screen = pygame.display.set_mode(self.menuResolution)

        pygame.init()
        menu = True

        # Valikko looppi
        while menu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

            # Main menu otsikko ja tausta
            self.menu_screen.fill(self.black)
            textCont = pygame.font.Font('OpenSans-Bold.ttf', 100)
            textSurf, textRect = self.text_object("KÄRMESPELI", textCont, self.white)
            textRect.center = (math.floor((self.menuWidth / 2)), 100)
            self.menu_screen.blit(textSurf, textRect)

            # Nappien luonti
            self.button("ALOITA PELI!", 160, 200, 500, 75, self.green, self.light_green, "play")
            self.button("SULJE PELI!", 160, 400, 500, 75, self.red, self.light_red, "quit")
            self.button("TEKIJÄT", 160, 300, 500, 75, self.gray, self.light_gray, "credits")

            pygame.display.update()
            self.clock.tick(15)

    # Tekijä valikko
    def credits(self):

        credits = True
        while credits:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

            self.menu_screen.fill((10, 10, 10))
            textCont = pygame.font.Font('OpenSans-Regular.ttf', 50)
            textSurf, textRect = self.text_object("Juhana Kuparinen", textCont, self.white)
            textRect.center = (400, 200)
            self.menu_screen.blit(textSurf, textRect)

            textCont = pygame.font.Font('OpenSans-Regular.ttf', 50)
            textSurf, textRect = self.text_object("Juho Ollila", textCont, self.white)
            textRect.center = (400, 300)
            self.menu_screen.blit(textSurf, textRect)

            textCont = pygame.font.Font('OpenSans-Regular.ttf', 50)
            textSurf, textRect = self.text_object("Johanna Seulu", textCont, self.white)
            textRect.center = (400, 400)
            self.menu_screen.blit(textSurf, textRect)

            pygame.display.update()
            pygame.time.wait(5000)
            self.main_menu()

    # Tason valinta valikko
    def level_select(self):
        pygame.quit()
        pygame.init()
        self.menuWidth = 800
        self.menuHeight = 600
        self.menuResolution = (self.menuWidth, self.menuHeight)
        self.menu_screen = pygame.display.set_mode(self.menuResolution)
        level = True
        while level:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
            self.menu_screen.fill(self.black)
            self.button("HELPPO", 160, 200, 500, 75, self.green, self.light_green, "easy")
            self.button("NORMAALI", 160, 300, 500, 75, self.yellow, self.light_yellow, "normal")
            self.button("VAIKEA", 160, 400, 500, 75, self.red, self.light_red, "hard")
            pygame.display.update()
            self.clock.tick(15)


#################################
# GAME LUOKKA
#################################

class Game:
    windowWidth = 800
    windowHeight = 600
    screenResolution = (windowWidth, windowHeight)
    clock = pygame.time.Clock()
    snake = 0
    score1 = 0
    score2 = 0

    # Pythonissa luokan konstruktori on __init__.
    # Luokan sisällä olevien funktioiden ensimmäinen argumentti on aina
    # olioon itseensä viittaavan muuttujan nimi (Javan this -avainsana).
    # Pythonissa on tapana nimittää tätä muuttujaa nimellä self,
    # mutta ohjelmoija voi halutessaan käyttää myös jotain muuta nimitystä tälle.
    def __init__(self, difficulty, gamemode):
        self.running = True
        self.last = pygame.time.get_ticks()
        self.cooldown = 100
        self.difficulty = difficulty
        self.gamemode = gamemode
        self.obstacles = []
        self.pause = False

    def game_loop(self):
        # Peli looppi
        self.apple.newApple(self.gridSize)
        # Jos vaikeustaso on "Hard", generoidaan esteitä
        if (self.difficulty.name == "Hard"):
            for i in range(random.randint(7, 15)):
                self.obstacles.append(Obstacle(self.windowWidth / self.gridSize, self.windowHeight / self.gridSize))
                self.obstacles[i].newObstacle(self.gridSize)

        while self.running:

            # Tapahtuma looppi
            for event in pygame.event.get():
                # Ensimmäinen if lause käsittelee pelistä poistumisen
                if event.type == QUIT:
                    pygame.quit()
                    quit()

                elif event.type == KEYDOWN:
                    now = pygame.time.get_ticks()
                    if event.key == K_ESCAPE:
                        menu = Menu()
                        menu.main_menu()

                    if event.key == K_SPACE:
                        self.pause = not self.pause

                    # Cooldowneilla estetään nappien spämmäys
                    # Pelaaja 1
                    if event.key == K_RIGHT and now - self.last >= self.cooldown:
                        self.last = now
                        self.snake.moveRight()

                    if event.key == K_LEFT and now - self.last >= self.cooldown:
                        self.last = now
                        self.snake.moveLeft()

                    if event.key == K_UP and now - self.last >= self.cooldown:
                        self.last = now
                        self.snake.moveUp()

                    if event.key == K_DOWN and now - self.last >= self.cooldown:
                        self.last = now
                        self.snake.moveDown()
                    # Pelaaja 2
                    if event.key == K_d and now - self.last >= self.cooldown:
                        self.last = now
                        self.other_snake.moveRight()

                    if event.key == K_a and now - self.last >= self.cooldown:
                        self.last = now
                        self.other_snake.moveLeft()

                    if event.key == K_w and now - self.last >= self.cooldown:
                        self.last = now
                        self.other_snake.moveUp()

                    if event.key == K_s and now - self.last >= self.cooldown:
                        self.last = now
                        self.other_snake.moveDown()

            # Onko peli pysäytetty?
            if not self.pause:
                # Varmistetaan että peli ei mene yli 10 fps:n (kärmes kulkee valonnopeudella muuten...)
                self.clock.tick(10)
                self.display_screen.fill((10, 10, 10))
                self.drawGrid()
                self.apple.drawApple()

                for i in range(len(self.obstacles)):
                    self.obstacles[i].drawObstacle()
                    if self.obstacles[i].obstacleLocation() == self.apple.appleLocation():
                        self.apple.newApple(self.gridSize)

                self.snake.update(self.gridSize)
                if self.gamemode.name == "Duel":
                    self.other_snake.update(self.gridSize)

                # Pisteiden näyttäminen ruudulla
                if self.gamemode.name == "Solo":
                    scoreText = "Pisteet: " + str(self.score1)
                    textCont = pygame.font.Font('OpenSans-Regular.ttf', 20)
                    textSurf, textRect = self.text_object(scoreText, textCont, (255, 255, 255))
                    textRect.center = (math.floor((self.windowWidth / 2)), 20)
                    self.display_screen.blit(textSurf, textRect)
                else:
                    # Pelaaja 1
                    scoreText1 = "Pisteet p1: " + str(self.score1)
                    textCont1 = pygame.font.Font('OpenSans-Regular.ttf', 20)
                    textSurf1, textRect1 = self.text_object(scoreText1, textCont1, (255, 255, 255))
                    textRect1.center = (math.floor((self.windowWidth / 2)), 20)
                    self.display_screen.blit(textSurf1, textRect1)

                    # Pelaaaja 2
                    scoreText2 = "Pisteet p2: " + str(self.score2)
                    textCont2 = pygame.font.Font('OpenSans-Regular.ttf', 20)
                    textSurf2, textRect2 = self.text_object(scoreText2, textCont2, (255, 255, 255))
                    textRect2.center = (math.floor((self.windowWidth / 2)), 60)
                    self.display_screen.blit(textSurf2, textRect2)

                # Törmäysten tunnistus
                if not self.snake.isOnScreen(int(self.windowWidth / self.gridSize), int(self.windowHeight / self.gridSize))\
                        or self.snake.collideWithSelf():
                    menu = Menu()
                    menu.main_menu()

                if self.gamemode.name == "Duel":
                    if not self.other_snake.isOnScreen(int(self.windowWidth / self.gridSize), int(self.windowHeight / self.gridSize)) or self.other_snake.collideWithSelf():
                        menu = Menu()
                        menu.main_menu()

                if self.snake.snakeLocation() == self.apple.appleLocation():
                    self.apple.newApple(self.gridSize)
                    self.snake.growSnake()
                    self.score1 += 1

                if self.other_snake.snakeLocation() == self.apple.appleLocation():
                    self.apple.newApple(self.gridSize)
                    self.other_snake.growSnake()
                    self.score2 += 1

                if self.snake.isOnApple(self.apple.appleLocation()) or self.other_snake.isOnApple(self.apple.appleLocation()):
                    self.apple.newApple(self.gridSize)

                for i in range(len(self.obstacles)):

                    if self.obstacles[i].obstacleLocation() == self.snake.snakeLocation()\
                            or self.obstacles[i].obstacleLocation() == self.other_snake.snakeLocation():
                        menu = Menu()
                        menu.main_menu()
            else:
                self.display_screen.fill((10, 10, 10))
                text = "Pysäytetty..."
                textContent = pygame.font.Font('OpenSans-Regular.ttf', 60)
                textSurface, textRectangle = self.text_object(text, textContent, (255, 255, 255))
                textRectangle.center = (math.floor((self.windowWidth / 2)), self.windowHeight / 2)
                self.display_screen.blit(textSurface, textRectangle)

            # Metodia update() kutsutaan, jotta näyttö päivittyy...
            pygame.display.update()

        print("Your score was: " + str(self.score))

    # Funktio jolla aloitetaan peli
    def start_game(self, width, height):
        # pygame.init() -metodia täytyy kutsua, jotta pelimoottori
        # käynnistyy.
        pygame.init()

        self.windowWidth = width
        self.windowHeight = height

        self.screenResolution = (self.windowWidth, self.windowHeight)

        # Määritellään näytön ominaisuuksia kuten resoluutio...
        self.display_screen = pygame.display.set_mode(self.screenResolution)
        self.gridSize = 20
        self.snake = Snake(self.windowWidth / self.gridSize, self.windowHeight / self.gridSize, (255, 0, 0))
        if self.gamemode.name == "Duel":
            self.other_snake = Snake(self.windowWidth / self.gridSize, (self.windowHeight / self.gridSize)+10, (0, 0, 255))
        else:
            # Jos emme pelaa duel modia, sijoitetaan p2 ulos kentältä jota se ei häiritse peliä
            self.other_snake = Snake(self.windowWidth / self.gridSize, self.windowHeight + 10, (0, 0, 255))
        self.apple = Apple(self.windowWidth / self.gridSize, self.windowHeight / self.gridSize)

        # ja title sekä ikoni...
        icon = pygame.image.load('icon.png')
        pygame.display.set_caption("Kärmespeli")
        pygame.display.set_icon(icon)

        # Käynnistetään itse peli...
        self.game_loop()

    # drawGrid() -metodi piirtää Kärmespeliin ruudukon
    def drawGrid(self):
        for i in range(math.floor(self.windowWidth / (self.gridSize))):
            for j in range(4, math.floor(self.windowHeight / (self.gridSize))):
                rect = pygame.Rect(i * self.gridSize, j * self.gridSize, self.gridSize, self.gridSize)
                # Piirretään ruudukko. If else lauseilla tarkistetaan minkä värinen
                # ruutu tulee olemaan.
                if i % 2 == 0:
                    if j % 2 == 0:
                        pygame.draw.rect(self.display_screen, (0, 255, 0), rect, 0)
                    else:
                        pygame.draw.rect(self.display_screen, (0, 230, 0), rect, 0)
                else:
                    if j % 2 == 0:
                        pygame.draw.rect(self.display_screen, (0, 230, 0), rect, 0)
                    else:
                        pygame.draw.rect(self.display_screen, (0, 255, 0), rect, 0)

    def text_object(self, text, font, colour):
        textSurface = font.render(text, True, colour)
        return textSurface, textSurface.get_rect()