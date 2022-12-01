"""
Логика пули игрока.
"""

import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, player_ship):
        """Создаём пулю в текущей позиции корабля"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 500, 10)
        self.bullet_color = 255, 255, 255
        self.bullet_speed = 3
        self.rect.centerx = player_ship.rect.centerx
        self.rect.top = player_ship.rect.top
        self.y = float(self.rect.y)

    def bullet_update(self):
        """Перемещение пули вверх"""
        self.y -= self.bullet_speed
        self.rect.y = self.y

    def shot_bullet(self):
        """Отрисовка пули на экране"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
