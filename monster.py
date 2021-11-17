#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import image
from pygame.sprite import Sprite
import pygame

class Monster(Sprite):
    def __init__(self,screen,backrect,row,column):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load("image/plane.png")
        self.rect=self.image.get_rect()
        self.imagerect=self.image.get_rect()
        self.x=backrect["x"]+self.imagerect.width+2*column*self.imagerect.width
        self.y=backrect["y"]+self.imagerect.height+2*row*self.imagerect.height
        self.fast=1.5





    def draw_plane(self):
        self.screen.blit(self.image,(self.x,self.y))

    def update(self):
        self.y+=self.fast
        self.rect.y=self.y
        self.rect.x=self.x