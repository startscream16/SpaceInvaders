import pygame
import sys

def run_game():
    # Инициирует игру и создает объект экрана
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Just Screen")
    
    # Назначение цвета фона
    bg_color = (100, 100, 100)
        
    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_q:
                    sys.exit()
        
        # При каждом прохоже цикла перерисовывается экран
        screen.fill(bg_color)
            
        # Отображение последнего прорисованного экрана
        pygame.display.flip()
        

run_game()
    
