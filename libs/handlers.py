#!/usr/bin/env python

import sys

from game import *
from sprites.stars import BigStar

def newgame(button):
    button.screen.context.active_screen = "newgame"

def startgame(button):
    specie = 1
    size = 1
    color = 1
    for sprite in button.screen.sprites.sprites():
        if hasattr(sprite,'group_id'):
            if sprite.group_id == 1 and sprite.selected == True:
                specie = sprite.get_value()
            elif sprite.group_id == 2 and sprite.selected == True:
                size = sprite.get_value()
            elif sprite.group_id == 3 and sprite.selected == True:
                color = sprite.get_value()

    button.screen.context.game.random(specie, size, color)
    button.screen.context.active_screen = "galaxy"
    button.screen.context.screens['galaxy'].reload_stars()

def end_turn(button):
    button.screen.context.turn += 1
    button.screen.turns_label.text = "%d" % button.screen.context.turn

def go_to_galaxy(button):
    button.screen.context.active_screen = "galaxy"

def go_to_menu(button):
    button.screen.context.active_screen = "menu"

def options(button):
    print button.rect.centerx
    print button.rect.centery

def exit(button):
    sys.exit()
