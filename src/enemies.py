import pygame as pg

class enemy:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = pg.Vector2(15, 15)
        self.color = (255, 0, 0)  # Red color
        self.velocity = pg.Vector2(300, 300)

    def draw(self, surface):
        pg.draw.rect(surface, self.color, (self.pos_x, self.pos_y, self.size.x, self.size.y))

    def trace_player(self, player_pos, delta_time):
        direction = pg.Vector2(player_pos[0] - self.pos_x, player_pos[1] - self.pos_y)
        if direction.length() > 0:
            direction = direction.normalize()
            self.pos_x += direction.x * self.velocity.x * delta_time
            self.pos_y += direction.y * self.velocity.y * delta_time