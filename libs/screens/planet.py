from galaxdustk.screen import BaseScreen

class PlanetScreen(BaseScreen):
    background_path = 'data/images/backgrounds/star.png'

    def __init__(self, context):
        super(PlanetScreen,self).__init__(context)
        screenrect = self.context.screen.get_rect()
