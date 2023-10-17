import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from alien_bullets import AlienBullet

def check_keydown_events(event, ai_settings, screen, stats, sb, play_button,
        ship, aliens, bullets, alien_bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        record_record(ai_settings, screen, stats, sb)
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, play_button, ship, aliens,
            bullets, alien_bullets)
        
def fire_bullet(ai_settings, screen, ship, bullets):
    """
    Выпускает пулю, воспроизводит звук выстрела, если максимум еще не достигнут
    """
    if len(bullets) < ai_settings.bullets_allowed:
        sound = pygame.mixer.Sound('sound/laserblast.mp3')
        sound.play()
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
def fire_alien_bullet(ai_settings, screen, aliens, alien_bullets):
    """
    Пришелец выпускает пулю, воспроизводит звук выстрела,
    если максимум пуль на экране не достигнут
    """
    if len(alien_bullets) <  ai_settings.alien_bullets_allowed:
        sound = pygame.mixer.Sound('sound/alienattack.mp3')
        sound.play()
        new_alien_bullet = AlienBullet(ai_settings, screen, aliens)
        alien_bullets.add(new_alien_bullet)

def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
        bullets, alien_bullets):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            record_record(ai_settings, screen, stats, sb)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb,
            play_button, ship, aliens, bullets, alien_bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                aliens, bullets, alien_bullets, mouse_x, mouse_y)

def record_record(ai_settings, screen, stats, sb):
    filename = 'record.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
        
    old_record = ''
    for line in lines:
        old_record = line
    
    if stats.high_score > int(old_record):
        with open(filename, 'w') as file_object:
            file_object.write(str(stats.high_score))
            
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
        bullets, alien_bullets, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, play_button, ship, aliens,
            bullets, alien_bullets)
        
def start_game(ai_settings, screen, stats, sb, play_button, ship, aliens,
    bullets, alien_bullets):
        """Инициализирует начало новой игры"""
        
        # Сброс игровых настроек
        ai_settings.initialize_dynamic_settings()
        
        # Указатель мыши скрывается
        pygame.mouse.set_visible(False)
        
        # Сброс игровой статистики
        stats.reset_stats()
        stats.game_active = True
        
        # Сброс изображений счетов и уровня
        sb.prep_images()
        
        # Очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()
        
        # Создание нового флота и размещение корабля в центре
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
                
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
        play_button, alien_bullets):
    """Обновляет изображения на экране и отображает новый экран"""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    
    # Все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    # Вывод пули пришельцев
    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_alien_bullet()
    
    # Прорисовка корабля
    ship.blitme()
    
    # Вывод счета
    sb.show_score()
    
    # Прорисовка пришельцев
    aliens.draw(screen)
    
    # Кнопка Play отображается в том случае, если игра неактивна
    if not stats.game_active:
        play_button.draw_button()
    
    # Отображение последнего прорисованного экрана
    pygame.display.flip()
    
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets,
        alien_bullets):
    """Обновляет позиции пуль и уничтожает старые пули"""
    # Обновление позиций пуль
    bullets.update()
    
    # Удаление пуль, вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens,
        bullets, alien_bullets)
        
def update_alien_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets,
        alien_bullets):
    """Обновляет позиции пуль пришельцев и уничтожает старые пули пришельцев"""
    # Обновление позиций пуль пришельцев
    alien_bullets.update()
    
    # Удаление пуль, вышкдших за край экрана
    screen_rect = screen.get_rect()
    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.top >= screen_rect.bottom:
            alien_bullets.remove(alien_bullet)
    check_alien_bullet_ship_collisions(ai_settings, screen, stats, sb, ship,
        aliens, bullets, alien_bullets)
    
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens,
        bullets, alien_bullets):
    """Обработка коллизий пуль с пришельцами"""
    # Удаление пуль и пришельцев, участвующих в коллизиях
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            sound = pygame.mixer.Sound('sound/aliencrash.mp3')
            sound.play()
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)
    
    if len(aliens) == 0:
        start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets,
                alien_bullets)

def check_alien_bullet_ship_collisions(ai_settings, screen, stats, sb, ship,
        aliens, bullets, alien_bullets):
    """Обработка коллизий пуль пришельцев с кораблем"""
    # Удаление пуль пришельцев и уничтожение корабля
    if pygame.sprite.spritecollideany(ship, alien_bullets):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, 
            alien_bullets)
        
def start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets,
        alien_bullets):
    """Запускает новый уровень после уничтожения всех пришельцев"""
    # Уничтожение существующих пуль, повышение скорости
    bullets.empty()
    alien_bullets.empty()
    ai_settings.increase_speed()
        
    # Увеличение уровня
    stats.level += 1
    sb.prep_level()
        
    # Создание нового флота
    create_fleet(ai_settings, screen, ship, aliens)
        
def check_high_score(stats, sb):
    """Проверяет, появился ли новый рекорд"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
    
def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет количество рядов, помещающихся на экране"""
    available_space_y = (ai_settings.screen_height - 
        (3 * alien_height))
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number + 5
    aliens.add(alien)
    
def create_fleet(ai_settings, screen, ship, aliens):
    """Создает флот пришельцев"""
    # Создание пришельца и вычисление количества пришельцев в ряду
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
    
    # Создание флота пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
            
def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижение пришельцем края экрана"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Опускает весь флот и меняет направление флота"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets,
        alien_bullets):
    """Обрабатывает столкновение корабля с пришельцем"""
    if stats.ships_left > 0:
        # Воспроизводит звук крушения корабля
        sound = pygame.mixer.Sound('sound/shipcrash.mp3')
        sound.play()
        
        # Уменьшение ships_left
        stats.ships_left -= 1
        
        # Обновление игровой информации
        sb.prep_ships()
        
        # Очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()
        
        # Создание нового флота и размещение корабля в центре
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
        # Пауза
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets,
        alien_bullets):
    """Проверяет, добрались ли пришельцы до нижнего края экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Происходит то же, что и при столкновении с кораблем
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets,
                alien_bullets)
            break
                        
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets,
        alien_bullets):
    """
    Проверяет, достиг ли флот края экрана,
    после чего обновляет позиции всех пришельцев во флоте
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # Проыерка коллизий "пришелец-корабль"
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets,
                alien_bullets)
    
    # Проверка пришельцев, добравшихся до нижнего края экрана
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets,
        alien_bullets)
