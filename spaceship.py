#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame


class Spaceship():
    def __init__(self,screen,backrect):
        self.screen=screen
        self.image=pygame.image.load("./image/hero.png")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.move_right=False
        self.move_left=False
        self.move_up=False
        self.move_down=False
        self.backrect=backrect


    def drawShip(self):
        self.screen.blit(self.image,self.rect)


    def update(self):
        if self.move_left:
            if self.rect.x<self.backrect["x"]:
                return
            self.rect.centerx-=1
        elif self.move_right:
            if self.rect.bottomright[0]>self.backrect["x"]+self.backrect["width"]:
                return
            self.rect.centerx+=1
        elif self.move_up:
            if self.rect.topleft[1]<self.screen_rect.topleft[1]:
                return
            self.rect.centery-=1
        elif self.move_down:
            if self.rect.bottomright[1]>self.screen_rect.bottomright[1]:
                return
            self.rect.centery+=1