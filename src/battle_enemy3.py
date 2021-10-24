from pygame.sprite import Sprite
import pygame
import random as r
from config import *


class BattleEnemy3(Sprite):

    def __init__(self, x, y, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.direction = RIGHT
        #self.direction_x = direction_x #used to have self.direction_x as a parameter in innit
        self.size = size
        self.speed = 6
        self.player_float_timer = PLAYER_FLOAT_DELAY

        self.right_images = []
        self.left_images = []
        for idx in range(1,2):
            self.image = pygame.image.load(f'assets/Avatar_Temmie_right.png')
            self.image = pygame.transform.scale(self.image, (int(size * 2), (int(size * 2))))
            self.left_images.append(self.image)

            # self.screen.blit(self.image, (self.x, self.y))

            right_image = pygame.transform.flip(self.image, True, False)
            self.right_images.append(right_image)

            self.image_index = 0

            # self.player_flap_timer = PLAYER_FLAP_DELAY

            if self.direction == RIGHT:
                self.images = self.right_images
                #self.direction_x = self.right_direction_x
            if self.direction == LEFT:
                self.images = self.left_images
                #self.direction_x = self.left_direction_x

            self.image = self.get_next_image()
            self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.health = 7


        # self.images = []

        # self.images.append(img)
        # self.image_index = 0
        # image = self.images[0]


    def get_next_image(self):
        self.player_float_timer -= 1
        if self.player_float_timer == 0:
            self.player_float_timer = PLAYER_FLOAT_DELAY
            self.image_index += 1
        if self.image_index == len(self.images):
            self.image_index = 0
        if self.direction == RIGHT:
            self.images = self.right_images
        if self.direction == LEFT:
            self.images = self.left_images
        return self.images[self.image_index]

    def reset_battle_enemy_3(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.health = 7

    def update(self):
        # self.screen.blit(self.image, (self.x, self.y))

        self.image = self.get_next_image()
        
        self.rect.x = self.x
        self.rect.y = self.y

       # use directions: if left direction move left when x == 900, if right direction move right when x == 100
        """
        if self.x == 100:
            right_x
        if self.x == 099

        if self.x >= 100:
            self.x += self.speed
        if self.x >= 100 and self.x <= 900: 
            self.x -= self.speed
        """

        """
        self.right_direction_x += self.speed
        self.left_direction_x -= self.speed

        if self.x == 100:
            self.x += self.speed
            self.right_direction_x = RIGHT
        if self.x == 900:
            self.x -= self.speed
            self.left_direction_x = LEFT
            #note: move the codes in squiggly lines to the innit method? probably no.no need to

        
        if 100 <= self.x < 900:
            self.x += self.speed
        if self.x == 900:
            self.x -= self.speed
        """

        start_x = 100
        end_x = 900

        if self.direction == RIGHT:
            self.x += self.speed
        if self.direction == LEFT:
            self.images = self.left_images
            self.x -= self.speed
            # self.direction_x = self.left_direction_x

        if self.x <= start_x:
            self.direction = RIGHT
            # self.x += self.speed
        if self.x >= end_x:
            self.direction = LEFT
            # self.x -= self.speed

        # image = self.get_next_image()

        if DEBUG_MODE:
            pygame.draw.rect(self.screen, BLUE, self.rect)
        self.screen.blit(self.image, (self.x, self.y))

