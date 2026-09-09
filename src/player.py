import pygame as pg
from settings import *


class Player:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        
        self.pos_x = win_res.x / 2
        self.pos_y = win_res.y / 2
        self.size = 50
        self.color = (0, 255, 0)  # Green color
        self.velocity = pg.Vector2(500, 500)
        self._initialized = True

    def draw(self, surface):
        pg.draw.rect(surface, self.color, (self.pos_x, self.pos_y, self.size, self.size))

    def move(self, delta_time):
        keys = pg.key.get_pressed()

        direction = pg.Vector2(
            keys[pg.K_d] or keys[pg.K_RIGHT]
            - (keys[pg.K_a] or keys[pg.K_LEFT]),
            keys[pg.K_s] or keys[pg.K_DOWN]
            - (keys[pg.K_w] or keys[pg.K_UP]),
        )

        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.pos_x += direction.x * self.velocity.x * delta_time
            self.pos_y += direction.y * self.velocity.y * delta_time

        self.pos_x = max(0, min(self.pos_x, win_res.x - self.size))
        self.pos_y = max(0, min(self.pos_y, win_res.y - self.size))