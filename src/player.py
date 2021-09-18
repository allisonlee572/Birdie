from pygame.sprite import Sprite
import pygame
import random as r
from config import *


class Player(Sprite):

    def __init__(self, x, y, direction, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.direction = direction
        self.size = size
        self.screen = screen

        self.speed = 6

        image = pygame.image.load(f'assets/Avatar_MAGI_front.png')
        # self.screen.blit(self.image, (self.x, self.y))

        # self.image_index = 0

        # self.images = []

        # for number in range(1, 3):
            # img = pygame.image.load(f'assets/images/imagefiles{number}.png')
            # img = pygame.transform.scale(img, (size, size))

        # self.images.append(img)
        # self.image_index = 0
        # image = self.images[0]
        self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())

    def update(self):
        self.screen.blit(self.image, (self.x, self.y))

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
            self.y -= self.speed
        if keys_pressed[pygame.K_a]:
            self.x -= self.speed
            self.direction = LEFT
        if keys_pressed[pygame.K_s]:
            self.y += self.speed
        if keys_pressed[pygame.K_d]:
            self.x += self.speed
            self.direction = RIGHT
        
        self.rect.x = self.x
        self.rect.y = self.y

        # image = self.get_next_image()

        """
        if DEBUG_MODE:
            pygame.draw.rect(self.screen, RED, self.rect)
            self.screen.blit(image, (self.x, self.y))
"""
