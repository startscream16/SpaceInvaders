import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/tank.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Каждый новый корабль появляется у левого края экрана в центре
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        
        # Сохранение вещественной координаты центра корабля
        self.centery = float(self.rect.centery)
        
        # Флаги перемещения
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Обновляет позицию корабля с учетом флагов"""
        # Обновляется атрибут center, не rect
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
            
        # Обновление атрибута rect на основании self.center
        self.rect.centery = self.centery
        
    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Размещает танк в центре нижней стороны"""
        self.centery = self.screen_rect.centery


