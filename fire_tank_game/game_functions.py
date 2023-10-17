import sys
import pygame
from bullet import Bullet
from tank import Ship
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускаяет пулю, если максимум еще не достигнут"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens,
        bullets):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship,
                aliens, bullets, mouse_x, mouse_y)
            
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
        bullets, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки Play"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        # Сброс игровых настроек
        ai_settings.initialize_dynamic_settings()
        
        # Сброс игровой статистики
        stats.reset_stats()
        stats.game_active = True
        
        # Очистка списка пуль
        bullets.empty()
        
        # Размещение танка в центре
        ship.center_ship()
                
def update_screen(ai_settings, screen, stats, ship, bullets, aliens, 
        play_button):
    """Обновляет изображения на экране и отображает новый экран"""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    
    # Все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    # Прорисовка корабля
    ship.blitme()
    
    # Вывод прямоугольника на экран
    for alien in aliens.sprites():
        alien.draw_alien()
        
    # Кнопка Play отображается в том случае, если игра неативна
    if not stats.game_active:
        play_button.draw_button()

    # Отображение последнего прорисованного экрана
    pygame.display.flip()

def create_alien(ai_settings, screen, aliens):
    """Создает прямоугольник"""
    alien = Alien(ai_settings, screen)
    aliens.add(alien)
    
def update_alien(ai_settings, stats, screen, ship, aliens):
    """Обновляет позицию прямоугольника"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижение прямоугольником края экрана"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Меняет направление прямоугольника"""
    ai_settings.fleet_direction *= -1
    
def update_bullets(ai_settings, stats, screen, ship, aliens, bullets):
    """Обновляет позиции пуль и уничтожает старые пули"""
    # Обновление позиций пуль
    bullets.update()

    # Проверка попаданий в прямоугольник
    # При обнаружении попадания удалить пулю
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, False)
    
    # Увеличение скорости игры
    if collisions:
        ai_settings.increase_speed()
    
    check_bullets_right(ai_settings, stats, screen, ship, aliens, bullets)
    
def check_bullets_right(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.left >= ship.screen_rect.right:
            stats.lives_limit -= 1
            bullets.remove(bullet)
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
    
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Обрабатывает окончание игры"""
    if stats.lives_limit < 0:
        stats.game_active = False
        
