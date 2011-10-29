from galaxdustk.base import Widget
import pygame

def _go_to_star(widget):
    widget.screen.context.active_screen = "star"
    widget.screen.context.screens['star'].active_star = widget.star

class SmallStar(Widget):
    def __init__(self, screen, star):
        super(SmallStar,self).__init__(screen)
        self.star = star
        self.image = pygame.image.load('data/images/stars/star_%d.png' % star.star_type)
        self.rect = self.image.get_rect()
	self.connect('clicked', _go_to_star)
