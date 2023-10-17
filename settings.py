class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""
    
    def __init__(self):
        """Инициализирует статические настройки игры"""
        # Параметры экрана
        self.screen_width = 1285
        self.screen_height = 720
        self.bg_color = (0, 32, 48)
        
        # Настройки корабля
        self.ship_limit = 3
        
        # Параметры пуль
        self.bullet_width = 4
        self.bullet_height = 14
        self.bullet_color = 255, 140, 0
        self.bullets_allowed = 3
        
        # Параметры пуль пришельцев
        self.alien_bullet_width = 8
        self.alien_bullet_height = 8
        self.alien_bullet_color = 0, 127, 255
        self.alien_bullets_allowed = 1
        
        # Настройки пришельцев
        self.fleet_drop_speed = 10
        
        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 0.7
        self.bullet_speed_factor = 1.7
        self.alien_bullet_speed_factor = 0.2
        self.alien_speed_factor = 0.4
        
        # fleet_direction = 1 обозначает движение вправо, а = -1 влево
        self.fleet_direction = 1
        
        # Подсчет очков
        self.alien_points = 50
        
    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_bullet_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
