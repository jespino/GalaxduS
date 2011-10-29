import pygame
import os

class Label(pygame.sprite.Sprite):
    def __init__(self, label_text, font_size=24, font_color=(240, 240, 240)):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer

        self.text = label_text
        self.color = font_color

        self.font = pygame.font.Font(None, font_size)
        self.image = self.font.render(self.text, 1, self.color)
        self.image.convert()
        self.rect = self.image.get_rect()

    def update(self):
        self.image = self.font.render(self.text, 1, self.color)
        self.image.convert()
