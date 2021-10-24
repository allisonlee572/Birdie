from pygame.sprite import Sprite
import pygame
import random as r
from config import *


class Enemy3_Bullet1(Sprite):

    def __init__(self, x, y, size, direction, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen

        self.direction = direction

        self.image = pygame.image.load(f'assets/Enemy_Bullet.png')
        self.image = pygame.transform.scale(self.image, (int(size*1.0), size))
        if direction == DOWN:
            self.image = pygame.transform.flip(self.image, False, True)

        self.speed = 8

        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

        # img = pygame.image.load(f'assets/player-1.png')

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

        if DEBUG_MODE:
            pygame.draw.rect(self.screen, RED, self.rect)

        self.screen.blit(self.image, (self.x, self.y))
