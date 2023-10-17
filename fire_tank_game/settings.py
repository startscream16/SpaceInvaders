class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""
    
    def __init__(self):
        """Инициализирует статичные настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (1, 50, 32)
        
        # Настройки корабля
        self.ship_speed_factor = 0.5
        
        # Параметры пули
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = 255, 140, 0
        self.bullets_allowed = 3
        
        # Параметры прямоугольника
        self.alien_width = 50
        self.alien_height = 150
        self.alien_color = 255, 0, 0
        
        # Жизни игрока
        self.lives_available = 3
        
        # Темп ускорения игры
        self.speedup_scale = 3
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 0.7
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.3
        
        # fleet_direction = 1 обозначает движение вправо, а -1 влево
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

