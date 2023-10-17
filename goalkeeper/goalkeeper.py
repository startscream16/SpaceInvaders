import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Создание корабля и группы пришельцев
    ship = Ship(ai_settings, screen)
    aliens = Group()
    
    # Создание пришельца
    gf.create_alien(ai_settings, screen, aliens)
    
    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship)
        
        if ai_settings.game_active:
            # Обновление позиции корабля в ответ на события клавиатуры
            ship.update()
            # Обновляет позицию пришельца на экране
            gf.update_alien(ai_settings, screen, aliens, ship)
        # При каждом проходе цикла перерисовывается экран
        gf.update_screen(ai_settings, screen, ship, aliens)
        
run_game()

