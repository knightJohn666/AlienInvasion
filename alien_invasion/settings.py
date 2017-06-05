# coding=utf-8


class Settings(object):

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.gaem_title = "Alien Invasion"
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3
        self.ship_image_type_icon = 1
        self.ship_image_type_real = 0

        # 外星人设置
        self.fleet_drop_speed = 10

        # 子弹设置
        self.bullet_width = 20
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 0.5

        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50


    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print self.alien_points