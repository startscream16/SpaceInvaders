class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 32, 48)
        
        # Настройки пришельцев
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево
        self.fleet_direction = 1

