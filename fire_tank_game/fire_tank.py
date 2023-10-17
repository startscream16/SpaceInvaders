import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from tank import Ship
import game_functions as gf

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Создание кнопки Play
    play_button = Button(ai_settings, screen, "Play")
    
    # Создание корабля
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль
    bullets = Group()
    # Создание группы для хранения прямоугольников
    aliens = Group()
    
    # Создание пришельца
    gf.create_alien(ai_settings, screen, aliens)
    
    # Создание экземпляра для хранения статистики
    stats = GameStats(ai_settings)
    
    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens,
            bullets)
        
        if stats.game_active:
            # Обновление позиции корабля в ответ на события клавиатуры
            ship.update()
            # Обновление позиции пуль и уничтожение старых пуль
            gf.update_bullets(ai_settings, stats, screen, ship, aliens, bullets)
            # Обновление позиции прямоугольника
            gf.update_alien(ai_settings, stats, screen, ship, aliens)
            
        # При каждом проходе цикла перерисовывается экран
        gf.update_screen(ai_settings, screen, stats, ship, bullets, aliens,
            play_button)

run_game()

