from pygame.sprite import Sprite
import pygame
import random as r
from config import *

class HealthBorder(Sprite):

    def __init__(self, x, y, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen

        self.image = pygame.image.load(f'assets/Health Border.jpg')
        self.image = pygame.transform.scale(self.image, (int(size * 6.5), (int(size * 1.5))))

        # self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def update(self):
        # self.y += self.speed
        # self.rect.y = self.y

        # if DEBUG_MODE:
            # pygame.draw.rect(self.screen, RED, self.rect)

        self.screen.blit(self.image, (self.x, self.y))
