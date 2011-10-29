from galaxdustk.base import Widget

class SmallStar(Widget):
    def __init__(self, screen, star):
        super(StarSprite,self).__init__(screen)
        self.star = star
        self.image = pygame.image.load('data/images/stars/star_%d.png' % star.star_type)
        self.rect = self.image.get_rect()
