from galaxdustk.screen import BaseScreen
import pygame

class StarScreen(BaseScreen):
    background_path = 'data/images/backgrounds/star.png'

    def __init__(self, context):
        super(StarScreen,self).__init__(context)
