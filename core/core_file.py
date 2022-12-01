"""
Основной файл игры.
"""

import pygame
import button_controls
from pygame.sprite import Group
from player_ship import PlayerShip
from statis import Statis


def run():
    pygame.init()  # Инициализация ИГРЫ.
    screen = pygame.display.set_mode((700, 750))  # Графическая область.
    pygame.display.set_caption('Alien Invasion')  # Название окна.
    bg_color = (0, 0, 0)  # Заливка цветом.
    player_ship = PlayerShip(screen)
    bullet_list = Group()
    enemy = Group()
    button_controls.create_army(screen, enemy)
    statis = Statis()

    while True:  # Бесконечный цикл игры. Обработка действий игрока.
        button_controls.events(screen, player_ship, bullet_list)
        player_ship.update_ship()  # Отрисовка корабля.
        button_controls.update(bg_color, screen, player_ship, enemy,
                               bullet_list)
        button_controls.update_bullets(screen, enemy, bullet_list)
        button_controls.update_enemies(statis, screen,
                                       player_ship, enemy, bullet_list)


if __name__ == '__main__':
    run()
