# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 08:51:50 2019

@author: weixiao
"""

import pygame

from settings import Settings
from button import Button
from game_stats import GameStats
from ship import Ship
from scoreboard import Scoreboard
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    
    # 创建游戏基础设置
    ai_settings = Settings()
    
    # 创建游戏窗口
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    
    # 创建游戏名称
    pygame.display.set_caption("星际战争1.0")
    
    # 创建存储游戏数据的实例
    stats = GameStats(ai_settings)
    
    # 创建记分板
    sb = Scoreboard(ai_settings,screen,stats)
    
    # 创建play按钮
    play_button = Button(ai_settings,screen,"开始游戏")
    
    # 创建飞船
    ship = Ship(ai_settings,screen)
    # 创建子弹编组
    bullets = Group()
    # 创建外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
     
run_game()
"""运行游戏"""