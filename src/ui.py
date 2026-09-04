import pygame as pg
import random
from settings import *

score = 0
time = 0

# Function to draw the UI elements (score and time) on the screen
def draw_ui(surface, stars,elapsed_time):
    # Draw the score on the screen
    time = elapsed_time
    score = time * 10  # Increase score based on time elapsed
    font = pg.font.Font(None, 36)
    score_text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
    time_text = font.render(f"Time: {int(time)}s", True, (255, 255, 255))
    surface.blit(score_text, (10, 10))
    surface.blit(time_text, (10, 50))
    for star in stars:
        pg.draw.rect(surface, (255, 255, 255), star)  # Draw each star rectangle in yellow
