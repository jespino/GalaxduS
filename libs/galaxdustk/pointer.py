import pygame
import os

class Pointer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image_default = pygame.image.load('data/images/cursors/default_cursor.png')
        self.image_default.convert()

        self.image_hover = pygame.image.load('data/images/cursors/hover.png')
        self.image_hover.convert()

        self.image = self.image_default
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos

    def set_hover(self):
        self.image = self.image_hover

    def set_default(self):
        self.image = self.image_default
