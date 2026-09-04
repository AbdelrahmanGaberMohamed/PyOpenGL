import pygame as pg
import sys
import array
import moderngl as mgl
from settings import *
from shaders import *
from engine import game_engine
from player import Player


game = game_engine()
screen = pg.display.set_mode(win_res, pg.OPENGL | pg.DOUBLEBUF)
#pg.display.toggle_fullscreen()
display = pg.Surface((win_res[0], win_res[1]))
img = pg.image.load("my_game/assets/img.png")
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

# Main game loop
while game.running:
    game.handle_events()
    game.update()

    display.fill((0, 0, 0))  # Clear the display with black color
    player.draw(display)
    player.update(game.delta_time)
    frame_texture = surface_to_texture(display)
    frame_texture.use(0)  # Bind the texture to texture unit 0
    program['tex'] = 0  # Set the shader uniform to use texture unit 0
    render_object.render(mode=mgl.TRIANGLE_STRIP)  # Render the quad with the texture
    pg.display.flip()
    frame_texture.release()  # Release the texture after rendering

    