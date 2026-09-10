import pygame as pg

class Enemy:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = pg.Vector2(15, 15)
        self.color = (255, 0, 0)  # Red color
        self.velocity = pg.Vector2(150, 150)
        self.launch = False # Flag to determine if tragectory has been calcualted

    def draw(self, surface):
        pg.draw.rect(surface, self.color, (self.pos_x, self.pos_y, self.size.x, self.size.y))


    def move(self, player_pos, delta_time):
        if self.launch:
            pass
        else:
            self.launch = True
            direction = pg.Vector2(player_pos[0] - self.pos_x, player_pos[1] - self.pos_y)
            if direction.length() > 0:
                direction = direction.normalize()
                self.pos_x += direction.x * self.velocity.x * delta_time
                self.pos_y += direction.y * self.velocity.y * delta_time
        self.pos_x += self.velocity.x * delta_time
        self.pos_y += self.velocity.y * delta_time

    def track_player(self, player_pos, delta_time):
        direction = pg.Vector2(player_pos[0] - self.pos_x, player_pos[1] - self.pos_y)
        if direction.length() > 0:
            direction = direction.normalize()
            self.pos_x += direction.x * self.velocity.x * delta_time
            self.pos_y += direction.y * self.velocity.y * delta_time
