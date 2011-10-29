#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from constants import STAR_NAMES

class Game:
    players = []
    stars = []
    turn = 0

    def random(self, specie, size, color):
        ocupied_pixels = []
        for x in range(0,size*20):
            star = Star()
            star.name = STAR_NAMES[x]
            star.random()
            while star.position==(0,0) or star.position in ocupied_pixels:
                star.position = (random.randint(35,565), random.randint(35,565))
            for x in range(star.position[0]-15,star.position[0]+15):
                for y in range(star.position[1]-15,star.position[1]+15):
                    ocupied_pixels.append((x,y))
            self.stars.append(star)
            
        player = Player()
        player.player_type = "user"
        player.color = color
        player.specie = specie
        self.players.append(player)

        #for x in range(0,3):
        #    player = Player()
        #    player.color = 
        #    player.specie = 
        

class Player:
    owned_planets = []
    color = 0
    specie = 0
    player_type = "computer"

class Star:
    planets = []
    star_type = 0
    name = ""
    position = (0,0)

    def random(self):
        for x in range(0,random.randint(0,6)):
            planet = Planet()
            planet.random()
            planet.name = "%s - %d" % (self.name, x)
            self.planets.append(planet)
        self.star_type = random.randint(1,5)

class Planet:
    buildings = []
    planet_type = 0
    name = ""

    def random(self):
        self.planet_type = random.randint(1,5)

class Building:
    pass
