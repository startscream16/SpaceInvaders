import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
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
    
    # Создание экземпляров игровой статистики и Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Создание корабля, группы пуль и группы пришельцев
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    alien_bullets = Group()
    
    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Воспроизведение музыкальной темы
    pygame.mixer.music.load('sound/theme.mp3')
    pygame.mixer.music.play(-1)
    
    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets, alien_bullets)
        
        if stats.game_active:
            # Обновление позиции корабля в ответ на события клавиатуры
            ship.update()
            # Обновление позиции пуль и уничтожение старых пуль, коллизия
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets, alien_bullets)
            gf.fire_alien_bullet(ai_settings, screen, aliens, alien_bullets)
            # Обновление позиций пуль пришельцев и уничтожение старых пуль
            gf.update_alien_bullets(ai_settings, screen, stats, sb, ship,
                aliens, bullets, alien_bullets)
            # Обновление позиций пришельцев
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets, alien_bullets)

        # При каждом проходе цикла перерисовывается экран
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
            play_button, alien_bullets)
        
run_game()
