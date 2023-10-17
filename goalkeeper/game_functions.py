import sys
import pygame
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def create_alien(ai_settings, screen, aliens):
    """Создает одного пришельца"""
    alien = Alien(ai_settings, screen)
    aliens.add(alien)
    
def ship_hit(ai_settings, screen, ship, aliens):
    # Уменьшение ships_left
    if ai_settings.ships_left > 0:
        ai_settings.ships_left -= 1

    else:
        ai_settings.game_active = False
    
def check_aliens_bottom(ai_settings, screen, ship, aliens):
    # Проверяет достижение пришельцем нижнего края экрана
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.top >= screen_rect.bottom:
           ship_hit(ai_settings, screen, ship, aliens)
           break
    
def update_alien(ai_settings, screen, aliens, ship):
    """Обновляет позицию пришельца"""
    aliens.update(screen)
    
    # Удаление пришельцев, вышедших за край экрана
    screen_rect = screen.get_rect()

    # Проверка пришельцев, добравшихся до нижнего края экрана
    check_aliens_bottom(ai_settings, screen, ship, aliens)
   
    make_new_alien = False
    for alien in aliens.copy():
        if alien.rect.top >= screen_rect.bottom:
            aliens.remove(alien)
            make_new_alien = True
    if make_new_alien:
        create_alien(ai_settings, screen, aliens)
    
    if pygame.sprite.spritecollideany(ship, aliens):
        aliens.remove(alien)
        create_alien(ai_settings, screen, aliens)
                
def update_screen(ai_settings, screen, ship, aliens):
    """Обновляет изображения на экране и отображает новый экран"""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    
    # Прорисовка пришельца
    aliens.draw(screen)
        
    # Прорисовка корабля
    ship.blitme()
    
    # Отображение последнего прорисованного экрана
    pygame.display.flip()

