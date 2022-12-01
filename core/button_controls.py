"""
Управление кораблём и прочие клавиши.
"""

import pygame
import sys
import time
from bullet import Bullet
from enemy_ship import EnemyShip


def events(screen, player_ship, bullet_list):
    """Обработка событий, Нажатия клавиш"""
    for event in pygame.event.get():  # Отлов всех действий игрока.
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # Движение в право.
                player_ship.move_right = True
            elif event.key == pygame.K_a:  # Движение в лево.
                player_ship.move_left = True
            elif event.key == pygame.K_SPACE:  # Выстрел
                new_bullet = Bullet(screen, player_ship)
                bullet_list.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:  # Прекратить движение в право.
                player_ship.move_right = False
            elif event.key == pygame.K_a:  # Прекратить движение в лево.
                player_ship.move_left = False


def update(bg_color, screen, player_ship, enemies, bullet_list):
    screen.fill(bg_color)  # Заливка экрана указанным цветом.
    for bullet in bullet_list.sprites():
        bullet.shot_bullet()
        bullet.bullet_update()
    player_ship.output()  # Запуск метода корабля для отрисовки на экране.
    enemies.draw(screen)  # Запуск метода врага для отрисовки на экране.
    pygame.display.flip()  # Отображение последнего экрана.


def update_bullets(screen, enemies, bullet_list):
    """Обновлять позиции пуль"""
    bullet_list.update()
    for bullet in bullet_list.copy():
        if bullet.rect.bottom <= 0:
            bullet_list.remove(bullet)
    # print(len(bullet_list))  # Проверка на утечку памяти.
    collisions = pygame.sprite.groupcollide(bullet_list, enemies,
                                            True, True)
    if len(enemies) == 0:
        bullet_list.empty()
        time.sleep(2)
        create_army(screen, enemies)


def player_ship_kill(stats, screen, player_ship, enemy, bullets):
    """Столкновение корабля с врагами"""
    stats.player_ship_lost = -1
    enemy.empty()
    bullets.empty()
    create_army(screen, enemy)
    player_ship.create_player_ship()
    time.sleep(2)


def update_enemies(stats, screen, player_ship, enemy, bullets):
    """Обновляет позицию врагов"""
    enemy.update()
    if pygame.sprite.spritecollideany(player_ship, enemy):
        player_ship_kill(stats, screen, player_ship, enemy, bullets)
    enemies_check(stats, screen, player_ship, enemy, bullets)


def enemies_check(stats, screen, player_ship, enemy, bullets):
    """Добрались ли враги до края?"""
    screen_rect = screen.get_rect()
    for enemy in enemy.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            player_ship_kill(stats, screen, player_ship, enemy, bullets)
            break


def create_army(screen, enemies):
    """Создание армии врагов"""
    enemy = EnemyShip(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((700 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 70 - 2 * enemy_height) / enemy_height)

    for row_number in range(number_enemy_y - 2):
        for enemy_number in range(number_enemy_x):
            enemy = EnemyShip(screen)
            enemy.x = enemy_width + (enemy_width * enemy_number)
            enemy.y = enemy_height + (enemy_height * row_number)
            enemy.rect.x = enemy.x
            enemy.rect.y = \
                enemy.rect.height + enemy.rect.height * row_number
            enemies.add(enemy)
