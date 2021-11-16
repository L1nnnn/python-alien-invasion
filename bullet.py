#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self,screen,slip):
        super().__init__()
        self.image=pygame.image.load("image/bullet.png")
        self.screen=screen
        self.slip=slip
        self.x=slip.rect.x+20
        self.y=slip.rect.y+20
        self.fast=3


    def draw_bullet(self):
        print(self.x,self.y)
        self.screen.blit(self.image,(self.x,self.y))

    def update(self):
        self.y-=self.fast

  