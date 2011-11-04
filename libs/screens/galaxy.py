from galaxdustk.buttons import Button, CircularButton
from galaxdustk.label import Label
from galaxdustk.screen import BaseScreen
from sprites.stars import SmallStar

import handlers

from gettext import gettext as _

from pprint import pprint

class GalaxyScreen(BaseScreen):
    background_path = 'data/images/backgrounds/galaxy.png'

    def __init__(self, context):
        super(GalaxyScreen,self).__init__(context)
        screenrect = self.context.screen.get_rect()

        self.turns_label = Label("0")
        self.turns_label.rect.left = screenrect.right - 180
        self.turns_label.rect.centery = screenrect.top + 45
        self.sprites.add(self.turns_label)
        
        next_turn = CircularButton(self, 'data/images/icons/arrow.png', radius=20)
        next_turn.rect.right = screenrect.right - 60
        next_turn.rect.top = 80
        next_turn.group_id = 1
        self.sprites.add(next_turn)

        fast_turn = CircularButton(self, 'data/images/icons/double_arrow.png', radius=20)
        fast_turn.rect.right = screenrect.right - 10
        fast_turn.rect.top = 80
        fast_turn.group_id = 1
        self.sprites.add(fast_turn)

        main_menu = Button(self, _("Main menu"), width=180)
        main_menu.rect.right = screenrect.right - 10
        main_menu.rect.bottom = screenrect.bottom - 20
        main_menu.connect("clicked", handlers.go_to_menu)
        self.sprites.add(main_menu)

    def reload_stars(self):
        for star in self.context.game.stars:
            star_sprite = SmallStar(self, star)
            star_sprite.rect.centerx = star.position[0]
            star_sprite.rect.centery = star.position[1]
            self.sprites.add(star_sprite)
