import pygame
from pygame.sprite import Group
from drops_settings import Settings
import drops_game_functions as gf

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    aliens = Group()
    
    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, aliens)
    
    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen)
        # Обновление позиций пришельцев
        gf.update_aliens(ai_settings, screen, aliens)
        # При каждом проходе цикла перерисовывается экран
        gf.update_screen(ai_settings, screen, aliens)
        
run_game()

