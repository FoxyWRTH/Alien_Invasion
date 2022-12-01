"""
Логика корабля врагов.
"""

import pygame


class EnemyShip(pygame.sprite.Sprite):
    """Класс врага"""

    def __init__(self, screen):
        """Инициализация и установка начальной позиции"""
        super(EnemyShip, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('../resource/image/enemy_ship.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Отрисовка врага"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещение пришельцев"""
        self.y += 0.2
        self.rect.y = self.y
