import sys
import pygame
from drops_alien import Alien

def check_keydown_events(event, ai_settings, screen):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_q:
        sys.exit()

def check_events(ai_settings, screen):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen)
                
def update_screen(ai_settings, screen, aliens):
    """Обновляет изображения на экране и отображает новый экран"""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    # Прорисовка пришельцев
    aliens.draw(screen)
    
    # Отображение последнего прорисованного экрана
    pygame.display.flip()

def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду"""
    available_space_x = ai_settings.screen_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, alien_height):
    """Определяет количество рядов, помещающихся на экране"""
    available_space_y = ai_settings.screen_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    screen_rect = screen.get_rect()
    alien.rect.y = 2 * alien.rect.height * row_number
    alien.y = alien.rect.y
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens):
    """Создает флот пришельцев"""
    # Создание пришельца и вычисление количества пришельцев в ряду
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, alien.rect.height)
    
    # Создание флота пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def create_new_row(ai_settings, screen, aliens):
    """Создает новый ряд пришельцев"""
    # Создание пришельца и вычисление количества пришельцев в ряду
    # Интервал между соседними пришельцами равен одной ширине пришельца
    
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    
    # Создание первого ряда пришельцев
    for alien_number in range(number_aliens_x):
        # Создание пришельца и размещение его в ряду
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        screen_rect = screen.get_rect()
        alien.rect.y = screen_rect.top
        alien.y = alien.rect.y
        aliens.add(alien)

def update_aliens(ai_settings, screen, aliens):
    """
    Проверяет, достиг ли флот края экрана,
    после чего обновляет позиции всех пришельцев во флоте
    """
    aliens.update()
    
    make_new_drops = False
    for alien in aliens.sprites():
        if alien.check_edges():
            aliens.remove(alien)
            make_new_drops = True

    if make_new_drops:
        create_new_row(ai_settings, screen, aliens)
