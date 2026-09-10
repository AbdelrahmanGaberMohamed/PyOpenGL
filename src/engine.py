import pygame as pg
import sys
from settings import *

class Game_Engine():
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.delta_time = 0.0
        self.running = True

    def update(self):
        self.delta_time = self.clock.tick(tick_rate) / 1000.0  # Convert milliseconds to seconds
        self.time = pg.time.get_ticks() * 0.001  # Convert milliseconds to seconds


    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
        pg.quit()
        sys.exit()

