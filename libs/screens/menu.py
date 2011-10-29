from galaxdustk.buttons import Button
from galaxdustk.image import Image
from galaxdustk.screen import BaseScreen

import handlers

from gettext import gettext as _

class MenuScreen(BaseScreen):
    background_path = 'data/images/backgrounds/menu.png'

    def __init__(self, context):
        super(MenuScreen,self).__init__(context)
        screenrect = self.context.screen.get_rect()

        logo = Image("data/images/logo.png")
        logo.rect.centerx = screenrect.centerx
        logo.rect.centery = 100
        self.sprites.add(logo)

        newgame = Button(self, _("New game"))
        newgame.rect.right = screenrect.right - 30
        newgame.rect.centery = screenrect.centery - 100
        newgame.connect("clicked",handlers.newgame)
        self.sprites.add(newgame)

        newgame = Button(self, _("Return to game"))
        newgame.rect.right = screenrect.right - 30
        newgame.rect.centery = screenrect.centery - 50
        newgame.connect("clicked", handlers.go_to_galaxy)
        self.sprites.add(newgame)

        newgame = Button(self, _("Save game"))
        newgame.rect.right = screenrect.right - 30
        newgame.rect.centery = screenrect.centery
        self.sprites.add(newgame)
        
        newgame = Button(self, _("Load game"))
        newgame.rect.right = screenrect.right - 30
        newgame.rect.centery = screenrect.centery + 50
        self.sprites.add(newgame)

        options = Button(self, _("Options"))
        options.rect.right = screenrect.right - 30
        options.rect.centery = screenrect.centery + 100
        self.sprites.add(options)

        exit = Button(self, _("Exit"))
        exit.rect.right = screenrect.right - 30
        exit.rect.centery = screenrect.centery + 150
        exit.connect("clicked",handlers.exit)
        self.sprites.add(exit)
