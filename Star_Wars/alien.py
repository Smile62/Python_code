# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:09:49 2019

@author: 14771
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """外星人的类"""
    
    def __init__(self,ai_settings,screen):
        """初始化外星人并设置其初始位置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/StarFighter2-1.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
          
        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        
    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image,self.rect)
        
    def check_edges(self):
        """监测外星舰队的位置"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >=screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *self.ai_settings.fleet_direction)
        self.rect.x = self.x