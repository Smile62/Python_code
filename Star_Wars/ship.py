# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 20:49:43 2019

@author: 14771
"""

import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/StarFighter1-1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    
        # 飞船初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 存储用小数表示的飞船位置
        self.center = float(self.rect.centerx)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """根据标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx