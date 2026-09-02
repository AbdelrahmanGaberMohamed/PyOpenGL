import pygame
import sys
import time
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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

        self.pos_x = SCREEN_WIDTH / 2
        self.pos_y = SCREEN_HEIGHT / 2
        self.size = 50
        self.color = (0, 255, 0)  # Green color
        self.velocity = pygame.Vector2(500, 500)
        self._initialized = True

def main(): 
    pygame.init()

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    glClearColor(0, 0, 0, 1.0)
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
    glDisable(GL_DEPTH_TEST)

    clock = pygame.time.Clock()
    running = True
    # Initialize player
    player = Player()
    while running:
        delta_time = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            player.pos_x -= player.velocity.x * delta_time
        if keys[K_RIGHT] or keys[K_d]:
            player.pos_x += player.velocity.x * delta_time
        if keys[K_UP] or keys[K_w]:
            player.pos_y += player.velocity.y * delta_time
        if keys[K_DOWN] or keys[K_s]:
            player.pos_y -= player.velocity.y * delta_time
        # Here you would add your OpenGL rendering code
        # Draw the player
        glColor3f(*player.color)
        glBegin(GL_QUADS)
        glVertex2f(player.pos_x - player.size / 2, player.pos_y - player.size / 2)
        glVertex2f(player.pos_x + player.size / 2, player.pos_y - player.size / 2)
        glVertex2f(player.pos_x + player.size / 2, player.pos_y + player.size / 2)
        glVertex2f(player.pos_x - player.size / 2, player.pos_y + player.size / 2)
        glEnd()
        pygame.display.flip()
        
    pygame.quit()
if __name__ == "__main__":
    main()