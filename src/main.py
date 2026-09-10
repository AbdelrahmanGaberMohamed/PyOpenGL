from random import random

import pygame as pg
import sys
import array
import moderngl as mgl
from settings import *
from shaders import *
from engine import *
from player import *
from ui import *
from enemies import *


game = Game_Engine()
screen = pg.display.set_mode(win_res, pg.OPENGL | pg.DOUBLEBUF)
#pg.display.toggle_fullscreen()
display = pg.Surface((win_res[0], win_res[1]))
#img = pg.image.load("my_game/assets/img.png")
ctx = mgl.create_context()

# Define shaders and create a program
quad_buffer = ctx.buffer(data=array.array('f', [
    # postion (x, y), texture coordinates (u, v)
    -1.0, 1.0, 0.0, 0.0,  # Top-left
    1.0, 1.0, 1.0, 0.0,   # Top-right
    -1.0, -1.0, 0.0, 1.0,  # Bottom-left
    1.0, -1.0, 1.0, 1.0    # Bottom-right
]))

program = ctx.program(vertex_shader=vert_shader, fragment_shader=frag_shader)
render_object = ctx.vertex_array(program, [(quad_buffer, '2f 2f', 'vert', 'texcoord')])

# Function to convert a Pygame surface to a ModernGL texture
def surface_to_texture(surface):
    tex = ctx.texture(surface.get_size(), 4)
    tex.filter = (mgl.NEAREST, mgl.NEAREST)
    tex.swizzle = 'BGRA'
    tex.write(surface.get_view('1'))
    return tex


# Initialize player
player = Player()

# Generate random postions for drawing a starry background
stars = []
for i in range(100):  # Create 100 stars with random positions
    x = random.randint(0, display.get_width())
    y = random.randint(0, display.get_height())
    stars.append(pg.Rect(x, y, 1, 1))

# Intiate enemies
def random_spawn():
    x1 = random.randint(-20 , 0)
    x2 = random.randint(display.get_width() , display.get_width() + 5)
    y = random.randint(0, display.get_height())
    x = random.randint(1,2)
    match x:
        case 1: 
            return pg.Vector2(x1, y)
        case 2: 
            return pg.Vector2(x2, y)
spawn_point = random_spawn()
enemy1 = Enemy(spawn_point.x, spawn_point.y)

# 
elapsed_time = 0
enemy_spawn_rate = 1
enemies = []

# Main game loop
while game.running:
    # Game
    elapsed_time += game.delta_time
    game.handle_events()
    game.update()

    # Display
    display.fill((0, 0, 0))  # Clear the display with black color
    draw_ui(display, stars, elapsed_time)

    # Player
    player.draw(display)
    player.move(game.delta_time)

    # Enmeies
    if enemy_spawn_rate > random.randint(0,10):
        spawn = random_spawn()
        enemies.append(Enemy(spawn.x, spawn.y))
    for enemy in enemies:
        enemy.draw(display)
        enemy.track_player((player.pos_x, player.pos_y), game.delta_time)

    

    # Pygame to mgl texture
    frame_texture = surface_to_texture(display)
    frame_texture.use(0)  # Bind the texture to texture unit 0
    program['tex'] = 0  # Set the shader uniform to use texture unit 0
    render_object.render(mode=mgl.TRIANGLE_STRIP)  # Render the quad with the textures
    pg.display.flip()
    frame_texture.release()  # Release the texture after rendering

    