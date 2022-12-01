"""
Управление статистическими данными.
"""

import pygame


class Statis():
    """Отслеживает статистику."""

    def __init__(self):
        """Инициализация статистики"""
        self.reset_statis()

    def reset_statis(self):
        """Статистика изменяющаяся во время игры"""
        self.player_ship_lost = 2
