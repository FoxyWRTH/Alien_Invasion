"""
Логика корабля игрока.
"""

import pygame


class PlayerShip:

    def __init__(self, screen):
        """Инициализация корабля игрока"""
        self.screen = screen
        self.ship_image = pygame.image.load('../resource/image/ship.png')
        """Создаёт прямоугольник корабля"""
        self.rect = self.ship_image.get_rect()
        self.screen_rect = screen.get_rect()
        """Получаем центр прямоугольника."""
        self.rect.centerx = self.screen_rect.centerx
        """Преобразование в float для более гладкого движения"""
        self.center = float(self.rect.centerx)
        """Получаем нижнюю координату корабля."""
        self.rect.bottom = self.screen_rect.bottom

        self.move_right = False
        self.move_left = False

    def output(self):
        self.screen.blit(self.ship_image, self.rect)

    def update_ship(self):
        """Обновление позиции корабля."""
        # Ниже приведены условия движения Корабля и проверки выхода за край.
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 1.8
        elif self.move_left and self.rect.left > self.screen_rect.left:
            self.center += -1.8

        self.rect.centerx = self.center

    def create_player_ship(self):
        """Размещает корабль игрока"""
        self.center = self.screen_rect.centerx
