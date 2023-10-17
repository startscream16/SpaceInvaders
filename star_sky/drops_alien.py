import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца"""
    
    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/wather.bmp')
        self.rect = self.image.get_rect()
        
        # Каждый новый пришелц появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Сохранение точной позиции пришельца
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Выводит пришельца в текущем положении"""
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True
        else:
            return False
        
    def update(self):
        """Перемещает пришельца вправо"""
        self.y += (self.ai_settings.alien_speed_factor *
            self.ai_settings.fleet_direction)
        self.rect.y = self.y
