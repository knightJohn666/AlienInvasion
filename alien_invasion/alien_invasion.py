# coding=utf-8

import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_function as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.gaem_title)

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen, ai_settings.ship_image_type_real)

    # 创建外星人组
    aliens = Group()

    # 创建一个子弹编组
    bullets = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:

        # 监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 更新飞船信息
            ship.update()

            # 更新外星人信息
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

            # 更新子弹信息
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # 刷新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()