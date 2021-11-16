#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame import image

import game as g

from spaceship import Spaceship
from settings import Settings
from pygame.sprite import Group



def run_game():
    pygame.init
    settings = Settings(1000,800,(230,230,230))
    screen=pygame.display.set_mode((settings.width,settings.height))
    pygame.display.set_caption("飞机大战")
    backimage=pygame.image.load("image/background.png")
    imagerect=backimage.get_rect()
    backrect ={"x":imagerect.x+imagerect.width/2,
               "y":imagerect.y,
               "width":imagerect.width,
               "height":imagerect.height
    }
    ship=Spaceship(screen,backrect)
    bullets = Group()
    while True:
        g.check_event(screen,ship,bullets)
        screen.blit(backimage,(backrect["x"],backrect["y"]))
        ship.update()
        ship.drawShip()
        bullets.update()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip() 

                         

if __name__ == "__main__":
    run_game()
    