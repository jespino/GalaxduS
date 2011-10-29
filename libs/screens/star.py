from galaxdustk.screen import BaseScreen
import pygame

class StarScreen(BaseScreen):
    background_path = 'data/images/backgrounds/star.png'

    def __init__(self, context):
        super(StarScreen,self).__init__(context)
        screenrect = self.context.screen.get_rect()

        star = pygame.sprite.Sprite()
        star.image = pygame.image.load('data/images/stars/star_1.big.png')
        star.rect = star.image.get_rect()
        star.rect.left = screenrect.left+30
        star.rect.centery = screenrect.centery
        self.sprites.add(star)
