# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:52:22 2019

@author: 14771
"""
import pygame

class Settings():
    """存储《星球大战》的所有设置的类"""
    def __init__(self):
        """初始化游戏常量"""
        
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 800
        # self.bg_color = (230,230,230)
        self.bg_image = pygame.image.load('images/bgimage1.jpg')
        
        # 飞船设置
        self.ship_limit = 2
        
        # 子弹设置
        self.bullet_width = 4
        self.bullet_height = 12
        self.bullet_color = (192,192,192)
        self.bullets_allowed = 15
        
        # 外星人设置
        self.fleet_drop_speed = 20
        
        # 游戏节奏设置
        self.speedup_scale = 1.08
        self.score_scale = 1.2
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """初始化游戏变量"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        
        self.alien_speed_factor = 1
        self.fleet_direction = -1
        
        # 计分
        self.alien_points = 20

    def increase_speed(self):
        """加快游戏节奏"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        