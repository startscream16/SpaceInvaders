import pygame
from pygame.sprite import Sprite
import random

class AlienBullet(Sprite):
    """Класс для управления пулями, выпущеными пришельцами"""
    
    def __init__(self, ai_settings, screen, aliens):
        """Создает объект пули в текущей позиции случайного пришельца"""
        super().__init__()
        self.screen = screen
        screen_rect = screen.get_rect()
        
        # Создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.alien_bullet_width,
            ai_settings.alien_bullet_height)
            
        selected_alien = random.choice(aliens.sprites())

        self.rect.centerx = selected_alien.rect.centerx
        self.rect.top = selected_alien.rect.top
        
        # Позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)
        
        self.color = ai_settings.alien_bullet_color
        self.speed_factor = ai_settings.alien_bullet_speed_factor
        
    def update(self):
        """Перемещает пулю вверх по экрану"""
        # Обновление позиции пули в вещественном формате
        self.y += self.speed_factor
        # Обновление позиции прямоугольника
        self.rect.y = self.y
        
    def draw_alien_bullet(self):
        """Вывод пули на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
