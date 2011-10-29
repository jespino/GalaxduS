import pygame
import os

class Image(pygame.sprite.Sprite):
    def __init__(self, path):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
