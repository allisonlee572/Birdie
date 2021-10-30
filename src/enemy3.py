from pygame.sprite import Sprite
import pygame
import random as r
from config import *


class Enemy3(Sprite):

    def __init__(self, x, y, direction, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.direction = direction
        self.size = size
        self.speed = 6
        self.player_float_timer = IMAGE_DELAY

        self.right_images = []
        self.left_images = []
        for idx in range(1,2):
            self.image = pygame.image.load(f'assets/Avatar_Temmie_right.png')
            self.image = pygame.transform.scale(self.image, (int(size * 2), (int(size * 2))))
            self.right_images.append(self.image)

            # self.screen.blit(self.image, (self.x, self.y))

            left_image = pygame.transform.flip(self.image, True, False)
            self.left_images.append(left_image)

            self.image_index = 0

            # self.player_flap_timer = PLAYER_FLAP_DELAY

            if self.direction == RIGHT:
                self.images = self.right_images
            if self.direction == LEFT:
                self.images = self.left_images

            self.image = self.get_next_image()
            self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

        # self.images = []

        # self.images.append(img)
        # self.image_index = 0
        # image = self.images[0]

    def get_next_image(self):
        self.player_float_timer -= 1
        if self.player_float_timer == 0:
            self.player_float_timer = IMAGE_DELAY
            self.image_index += 1
        if self.image_index == len(self.images):
            self.image_index = 0
        if self.direction == RIGHT:
            self.images = self.right_images
        if self.direction == LEFT:
            self.images = self.left_images
        return self.images[self.image_index]

    def update(self):
        # self.screen.blit(self.image, (self.x, self.y))

        self.image = self.get_next_image()
        
        self.rect.x = self.x
        self.rect.y = self.y

        # image = self.get_next_image()

        if DEBUG_MODE:
            pygame.draw.rect(self.screen, RED, self.rect)
        self.screen.blit(self.image, (self.x, self.y))

