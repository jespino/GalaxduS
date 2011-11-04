from galaxdustk.base import Widget
import pygame

def _change_pointer_in(widget):
    widget.screen.context.pointer.set_hover()

def _change_pointer_out(widget):
    widget.screen.context.pointer.set_default()

def _go_to_star(widget):
    widget.screen.context.active_screen = "star"
    widget.screen.context.screens['star'].active_star = widget.star

    screenrect = widget.screen.context.screen.get_rect()

    widget.screen.context.screens['star'].sprites.empty()

    star = BigStar(widget.screen, widget.star)
    star.rect.centerx = screenrect.centerx
    star.rect.centery = screenrect.centery
    widget.screen.context.screens['star'].sprites.add(star)

class SmallStar(Widget):
    def __init__(self, screen, star):
        super(SmallStar,self).__init__(screen)
        self.star = star
        self.image = pygame.image.load('data/images/stars/star_%d.png' % star.star_type)
        self.rect = self.image.get_rect()
        self.connect('clicked', _go_to_star)
        self.connect('in', _change_pointer_in)
        self.connect('out', _change_pointer_out)

class BigStar(Widget):
    def __init__(self, screen, star):
        super(BigStar,self).__init__(screen)
        self.star = star
        self.image = pygame.image.load('data/images/stars/star_%d.big.png' % star.star_type)
        self.rect = self.image.get_rect()
