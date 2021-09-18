from pygame.sprite import Sprite
import pygame
import random as r
from config import *

"""
class Enemy(Sprite):

   def __init__(self, x, y, direction, size, screen):
       super().__init__()
       self.x = x
       self.y = y
       self.screen = screen
       self.size = size
       self.direction = direction

            self.left_images = []
       for idx in range(len(self.right_images)):
           self.right_images[idx] = pygame.transform.scale(self.right_images[idx], (int(size * 1.3), size))
           self.left_images.append(pygame.transform.flip(self.right_images[idx], True, False))

       if self.direction == RIGHT:
           self.images = self.right_images
       else:
           self.images = self.left_images

       self.speed = r.randint(1, 7)

       self.image_index = 0

       self.bird_flap_timer = BIRD_FLAP_DELAY
       image = self.get_next_image()
       self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())


"""
