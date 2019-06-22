# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:10:28 2019

@author: 14771
"""

class GameStats():
    """跟踪游戏统计信息"""
    
    def __init__(self,ai_settings):
        """初始化游戏数据"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 设置游戏状态
        self.game_active = False
        
    def reset_stats(self):
        """初始化游戏变量"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1