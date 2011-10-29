from galaxdustk.buttons import Button, CircularSelectButton, SelectButton
from galaxdustk.label import Label
from galaxdustk.screen import BaseScreen

import handlers

from gettext import gettext as _

class NewGameScreen(BaseScreen):
    background_path = 'data/images/backgrounds/menu.png'

    def __init__(self, context):
        super(NewGameScreen,self).__init__(context)
        screenrect = self.context.screen.get_rect()

        label_species = Label(_('Select your specie:'))
        label_species.rect.left = 10
        label_species.rect.centery = 100
        self.sprites.add(label_species)

        for x in range(1,4):
            specie = CircularSelectButton(self, 'data/images/species/specie%d.png' % x)
            specie.rect.left = (label_species.rect.right - 100) + (x*125)
            specie.rect.centery = 100
            specie.group_id = 1
            specie.value = x
            self.sprites.add(specie)

        label_size = Label(_('Select the galaxy size:'))
        label_size.rect.left = 10
        label_size.rect.centery = 200
        self.sprites.add(label_size)

        for galaxy_size in [(1,_('Small')),(2,_('Medium')),(3,_('Big'))]:
            size = SelectButton(self, galaxy_size[1], width=100)
            size.rect.left = (label_size.rect.right - 100) + (galaxy_size[0]*125)
            size.rect.centery = 200
            size.group_id = 2
            size.value = galaxy_size[0]
            self.sprites.add(size)

        label_size = Label(_('Select your color:'))
        label_size.rect.left = 10
        label_size.rect.centery = 300
        self.sprites.add(label_size)

        for player_color in [(1,_('Red'), (255,0,0)),(2,_('Green'), (0,255,0)),(3,_('Blue'), (0,0,255))]:
            one_color = SelectButton(self, player_color[1], width=100)
            one_color.rect.left = (label_size.rect.right - 100) + (player_color[0]*125)
            one_color.rect.centery = 300
            one_color.group_id = 3
            one_color.value = player_color[2]
            self.sprites.add(one_color)

        begin_game = Button(self, _("Begin the game"))
        begin_game.rect.right = screenrect.right - 10
        begin_game.rect.bottom = screenrect.bottom - 10
        begin_game.connect("clicked", handlers.startgame)
        self.sprites.add(begin_game)

        back = Button(self, _("Back"))
        back.rect.left = screenrect.left + 10
        back.rect.bottom = screenrect.bottom - 10
        back.connect("clicked", handlers.go_to_menu)
        self.sprites.add(back)
