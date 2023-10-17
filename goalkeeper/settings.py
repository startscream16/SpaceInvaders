class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 255, 255)
        
        # Настройки корабля
        self.ship_speed_factor = 0.7
        self.ships_left = 3
        
        # Настройки пришельцев
        self.drop_speed = 0.5
        
        self.game_active = True


