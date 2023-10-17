import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    """Класс, представляющий одного пришельца"""
    
    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()
        
        # Каждый новый пришелц появляется в случайном месте
        screen_rect = screen.get_rect()
        random_number = randint(0, screen_rect.right -
            (self.rect.width))
        self.rect.x = random_number
        self.rect.bottom = screen_rect.top
        
        # Сохранение точной позиции пришельца
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def draw_allien(self):
        """Выводит пришельца в текущем положении"""
        pygame.draw.rect(self.image, self.rect)
        
    def update(self, screen):
        """Перемещает пришельца вниз"""
        self.y += self.ai_settings.drop_speed
        self.rect.y = self.y

