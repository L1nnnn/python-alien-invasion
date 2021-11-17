#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

import sys

from pygame.sprite import Group

from bullet import Bullet
from monster import Monster

import random
 
def check_event(screen,ship,bullets,monsters):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:             
                if event.key==pygame.K_RIGHT:                  
                    ship.move_right=True
                elif event.key==pygame.K_LEFT:
                    ship.move_left=True
                elif event.key==pygame.K_DOWN:                 
                    ship.move_down=True
                elif event.key==pygame.K_UP:
                    ship.move_up=True
                elif event.key==pygame.K_SPACE:          
                    new_bullet = Bullet(screen,ship)
                    bullets.add(new_bullet)
            elif event.type==pygame.KEYUP:
                 ship.move_right=False
                 ship.move_left=False
                 ship.move_up=False     
                 ship.move_down=False

def add_monster(screen,monsters,backrect):
    for num in range(1,10):
        column=random.randint(0,5)
        row=random.randint(0,5)
        monster =Monster(screen,backrect,row,column)
        monsters.add(monster)
