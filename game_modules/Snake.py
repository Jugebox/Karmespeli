import pygame
import math
import random
from enum import Enum

# Snake luokka joka perii Sprite luokan
class Snake(pygame.sprite.Sprite):

    # Luodaan enum luokka, joka määrittelee käärmeen suunnat
    class Directions(Enum):
        Stop = 0
        Right = 1
        Left = 2
        Up = 3
        Down = 4

    direction = Directions.Right

    def __init__(self, width, height, color):
        self.rawHeadImg = pygame.image.load('pictures/Matopeli_mato_paa_' + color + '.png')
        self.rawBodyImg = pygame.image.load('pictures/Matopeli_mato_keski_' + color + '.png')
        self.rawTailImg = pygame.image.load('pictures/Matopeli_mato_hanta_' + color + '.png')

        self.rawHeadImg = pygame.transform.scale(self.rawHeadImg, (20, 20))
        self.rawBodyImg = pygame.transform.scale(self.rawBodyImg, (20, 20))
        self.rawTailImg = pygame.transform.scale(self.rawTailImg, (20, 20))

        self.headImg = self.rawHeadImg
        self.bodyImg = self.rawBodyImg
        self.tailImg = self.rawTailImg

        self.gridWidth = width
        self.gridHeight = height
        self.snake = [
                    [(int(self.gridWidth/2), int(self.gridHeight/2)), "Left"],
                    [(int(self.gridWidth/2)-1, int(self.gridHeight/2)), "Left"],
                    [(int(self.gridWidth/2)-2, int(self.gridHeight/2)), "Left"],
                    [(int(self.gridWidth/2)-3, int(self.gridHeight/2)), "Left"],
                    [(int(self.gridWidth/2)-4, int(self.gridHeight/2)), "Left"]
                      ]
        self.snakeHead = self.snake[0]
        self.color = color

    # update() metodilla liikutamme käärmettä.
    def update(self, gridSize):
        if self.direction == self.Directions.Right:
            self.headImg = pygame.transform.rotate(self.rawHeadImg, -90)
            newSnake = []
            x, y = self.snake[0][0]
            newSnake.append([(x+1, y), self.direction.name])
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        if self.direction == self.Directions.Left:
            self.headImg = pygame.transform.rotate(self.rawHeadImg, 90)
            newSnake = []
            x, y = self.snake[0][0]
            newSnake.append([(x-1, y), self.direction.name])
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        if self.direction == self.Directions.Up:
            self.headImg = pygame.transform.rotate(self.rawHeadImg, 0)
            newSnake = []
            x, y = self.snake[0][0]
            newSnake.append([(x, y-1), self.direction.name])
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        if self.direction == self.Directions.Down:
            self.headImg = pygame.transform.rotate(self.rawHeadImg, 180)
            newSnake = []
            x, y = self.snake[0][0]
            newSnake.append([(x, y+1), self.direction.name])
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        # Päivitetään pään sijainti
        self.snakeHead = self.snake[0]
        # Käärmeen piirtäminen
        for i in range(len(self.snake)):
            x, y = self.snake[i][0]
            rect = pygame.Rect(x * gridSize, y * gridSize, gridSize, gridSize)

            # Käännetään kuvakkeita kehon suunnan mukaan
            if self.snake[i][1] == "Up":
                self.bodyImg = pygame.transform.rotate(self.rawBodyImg, 0)
                self.tailImg = pygame.transform.rotate(self.rawTailImg, 0)
            if self.snake[i][1] == "Down":
                self.bodyImg = pygame.transform.rotate(self.rawBodyImg, 180)
                self.tailImg = pygame.transform.rotate(self.rawTailImg, 180)
            if self.snake[i][1] == "Right":
                self.bodyImg = pygame.transform.rotate(self.rawBodyImg, -90)
                self.tailImg = pygame.transform.rotate(self.rawTailImg, -90)
            if self.snake[i][1] == "Left":
                self.bodyImg = pygame.transform.rotate(self.rawBodyImg, 90)
                self.tailImg = pygame.transform.rotate(self.rawTailImg, 90)

            if i == 0:
                pygame.display.get_surface().blit(self.headImg, rect)
            elif i < len(self.snake)-1:
                pygame.display.get_surface().blit(self.bodyImg, rect)
            else:
                pygame.display.get_surface().blit(self.tailImg, rect)
            #pygame.draw.rect(pygame.display.get_surface(), self.color, rect, 0)
            '''# Gradientti kärmes
            if 255-(i*2) > 0:
                pygame.draw.rect(pygame.display.get_surface(), (255-(i*2), 0, 0), rect, 0)
            else:
                pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), rect, 0)
            '''
    # Metodit, joilla vaihdetaan käärmeen suuntaa.
    def moveRight(self):
        if self.direction != self.Directions.Left:
            self.direction = self.Directions.Right

    def moveLeft(self):
        if self.direction != self.Directions.Right:
            self.direction = self.Directions.Left

    def moveUp(self):
        if self.direction != self.Directions.Down:
            self.direction = self.Directions.Up

    def moveDown(self):
        if self.direction != self.Directions.Up:
            self.direction = self.Directions.Down

    def snakeLocation(self):
        return self.snake[0][0]

    def growSnake(self):
        x, y = self.snake[len(self.snake)-1][0]
        if self.direction != 2:
            self.snake.append([(x-1, y), self.snake[len(self.snake)-1][1]])
        else:
            self.snake.append([(x+1, y), self.snake[len(self.snake)-1][1]])

    def isOnScreen(self, width, height):
        x, y = self.snake[0][0]
        if x >= width or y >= height or x < 0 or y < 4:
            return False
        return True

    def isOnApple(self, appleLocation):
        for i in range(len(self.snake)):
            if self.snake[i][0] == appleLocation:
                return True
        return False

    def collideWithSelf(self):
        for i in range(1, len(self.snake)):
            if self.snake[0][0] == self.snake[i][0]:
                return True
        return False

    def collideWithOther(self, other):
        for i in range(0, len(self.snake)):
            if other == self.snake[i][0]:
                return True
        return False