import pygame as pg
import sys
import time
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from settings import *
import sys
import moderngl as mgl


class game_engine():
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.delta_time = 0.0
        self.running = True

    def update(self):
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001  # Convert milliseconds to seconds
        pg.display.set_caption(f"FPS: {self.clock.get_fps():.0f}")
        

    def render(self):
        img = pg.image.load("my_game/assets/img.png")
        screen = pg.display.set_mode(WIN_RES)
        screen.fill((0, 0, 0))  # Clear the screen with black color
        screen.blit(img, pg.mouse.get_pos())  # Draw the image at the mouse position
        pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
\
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()

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

        self.pos_x = WIN_RES.x / 2
        self.pos_y = WIN_RES.y / 2
        self.size = 50
        self.color = (0, 255, 0)  # Green color
        self.velocity = pg.Vector2(500, 500)
        self._initialized = True



    
def main(): 
    pg.init()

    pg.display.set_mode(WIN_RES, flags= pg.DOUBLEBUF | pg.OPENGL)
    glClearColor(0, 0, 0, 1.0)
    gluOrtho2D(0, WIN_RES.x, 0, WIN_RES.y)
    glDisable(GL_DEPTH_TEST)

    clock = pg.time.Clock()
    running = True
    # Initialize player
    player = Player()
    while running:
        delta_time = clock.tick(60) / 1000.0

        for event in pg.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Handle player movement
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            player.pos_x -= player.velocity.x * delta_time
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            player.pos_x += player.velocity.x * delta_time
        if keys[pg.K_UP] or keys[pg.K_w]:
            player.pos_y += player.velocity.y * delta_time
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            player.pos_y -= player.velocity.y * delta_time
        # Here you would add your OpenGL rendering code
        pg.display.flip()
        
    pg.quit()
if __name__ == "__main__":
    app = game_engine()
    app.run()