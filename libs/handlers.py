#!/usr/bin/env python

import sys

from game import *

def newgame(button):
    button.screen.context.active_screen = "newgame"

def startgame(button):
    specie = None
    size = None
    color = None
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

def go_to_star(button):
    button.screen.context.active_screen = "star"
    button.screen.context.screens['star'].active_star = button.star
    #button.screen.context.screens['star'].background_path = pygame.load("images/backgrounds/star_%d.png" % button.star.star_type)

def options(button):
    print button.rect.centerx
    print button.rect.centery

def exit(button):
    sys.exit()
