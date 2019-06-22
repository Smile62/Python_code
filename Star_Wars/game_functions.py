# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:33:20 2019

@author: 14771
"""

from sys import exit
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        exit()
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ai_settings,screen,ship,bullets):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """玩家单击Play开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    
    if button_clicked and not stats.game_active:
        
        # 重置游戏节奏
        ai_settings.initialize_dynamic_settings()
        
        # 隐藏光标
        pygame.mouse.set_visible(False)
        
        # 重置游戏数据
        stats.reset_stats()
        stats.game_active = True
        
        #重置游戏状态信息图像
        sb.prep_score()
        sb.prep_level()
        
        # 清空外形舰队和子弹
        aliens.empty()
        bullets.empty()
        
        # 创建新的外星舰队
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
        

def fire_bullet(ai_settings,screen,ship,bullets):
    """发射子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    # 删除发生碰撞的子弹和外星人
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)
      
def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
    if len(aliens) == 0:
        #新建一群外星人
        #bullets.empty()
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)

def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可容纳外星人数"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建外星人"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人舰队"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    alien = Alien(ai_settings,screen)
    number_alien_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    # 创建外星人舰队
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
        
def check_fleet_edges(ai_settings,aliens):
    """外形舰队到达屏幕边缘采取措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
        
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检测外星人是否到达底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
        
def change_fleet_direction(ai_settings,aliens):
    """改变外星舰队移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """更新外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    
    # 检测外星人和飞船的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
        
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """撞击事件"""
    if stats.ships_left  > 0:
        stats.ships_left -= 1
        
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        
        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
    
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    # 更新屏幕
    screen.blit(ai_settings.bg_image,(0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.prep_limit()
    # 显示得分
    sb.show_score()
    
    if not stats.game_active:
        play_button.draw_button()
    # 显示最近绘制的屏幕
    pygame.display.flip()