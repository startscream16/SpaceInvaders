import pygame

from settings_rocketman import Settings
from rocket import Ship
import game_functions_rocketman as gfr

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Создание корабля
    ship = Ship(ai_settings, screen)
    
    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gfr.check_events(ship)
        # Обновление позиции корабля в ответ на события клавиатуры
        ship.update()
        # При каждом проходе цикла перерисовывается экран
        gfr.update_screen(ai_settings, screen, ship)
        
run_game()

