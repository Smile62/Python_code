# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 21:42:20 2019

@author: 14771
"""

import pygame.font

class Scoreboard():
    """显示得分信息"""
    
    def __init__(self,ai_settings,screen,stats):
        """初始化游戏状态信息属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # 游戏状态信息字体设置
        self.text_color = (192,192,192)
        self.font = pygame.font.SysFont('simsunnsimsun',28)
        
        # 游戏状态信息图像
        self.prep_score()
        self.prep_level()
    
    def prep_score(self):
        """将分数文本渲染为图像"""
        round_score = int(round(self.stats.score,-1)) # Python3可省略int()
        score_str = "得分：" + "{:,}".format(round_score)
        self.score_image = self.font.render(score_str,True,self.text_color)
        
        #将分数在右上角显示
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_level(self):
        """将等级文本渲染为图像"""
        self.level_image = self.font.render("等级：" + str(self.stats.level),True,self.text_color)
        # 等级文本位置
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_limit(self):
        self.limits = self.stats.ships_left
        self.limit_image = pygame.image.load('images/StarFighter1-2.png')
        self.limit_rect = self.limit_image.get_rect()
        self.limit_rect.top = 20
        
        for limit in range(self.limits):
            self.limit_rect.left = 5 * (limit + 1) + 20 * limit
            self.screen.blit(self.limit_image,self.limit_rect)
            
    def show_score(self):
        """显示游戏状态信息"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)