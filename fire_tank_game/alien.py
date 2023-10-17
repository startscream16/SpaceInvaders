import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс для создания и управления прямоугольником"""
    
    def __init__(self, ai_settings, screen):
        """Создает объект прямоугольника в левом верхнем крае экрана"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        
        # Создание прямоугольника в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.alien_width,
            ai_settings.alien_height)
        self.rect.right = self.screen_rect.right - 10
        self.rect.top = self.screen_rect.top + 10
        
        # Позиция прямоугольника хранится в вещественном формате
        self.x = float(self.rect.right)
        self.y = float(self.rect.top)
        
        self.color = ai_settings.alien_color
        self.speed_factor = ai_settings.alien_speed_factor
        
    def check_edges(self):
        """Возвращает True, если прямоугольник находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True        

    def update(self):
        """Перемещает пулю вверх по экрану"""
        # Обновление позиции прямоугольника в вещественном формате
        self.y += (self.ai_settings.alien_speed_factor *
            self.ai_settings.fleet_direction)        
        # Обновление позиции прямоугольника
        self.rect.y = self.y
        
    def draw_alien(self):
        """Вывод прямоугольника на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)

