import pygame as pg
import sys
import array
import moderngl as mgl
from settings import *

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

game = game_engine()
screen = pg.display.set_mode(WIN_RES, pg.OPENGL | pg.DOUBLEBUF)
display = pg.Surface((WIN_RES[0], WIN_RES[1]))
img = pg.image.load("my_game/assets/img.png")
ctx = mgl.create_context()

quad_buffer = ctx.buffer(data=array.array('f', [
    # postion (x, y), texture coordinates (u, v)
    -1.0, 1.0, 0.0, 0.0,  # Top-left
    1.0, 1.0, 1.0, 0.0,   # Top-right
    -1.0, -1.0, 0.0, 1.0,  # Bottom-left
    1.0, -1.0, 1.0, 1.0    # Bottom-right
]))

vert_shader= '''
#version 330 core

in vec2 vert;
in vec2 texcoord;
out vec2 uvs;

void main() {
    uvs = texcoord;
    gl_Position = vec4(vert, 0.0, 1.0);
}
'''
frag_shader = '''
#version 330 core

in vec2 uvs;
out vec4 f_color;

uniform sampler2D tex;

void main() {
    f_color = vec4(texture(tex, uvs).rgb, 1.0);
}
'''

program = ctx.program(vertex_shader=vert_shader, fragment_shader=frag_shader)
render_object = ctx.vertex_array(program, [(quad_buffer, '2f 2f', 'vert', 'texcoord')])

def surface_to_texture(surface):
    #Convert a Pygame surface to a ModernGL texture.
    tex = ctx.texture(surface.get_size(), 4)
    tex.filter = (mgl.NEAREST, mgl.NEAREST)
    tex.swizzle = 'BGRA'
    tex.write(surface.get_view('1'))
    return tex


while game.running:
    game.handle_events()

    display.fill((0, 0, 0))  # Clear the display with black color
    display.blit(img, pg.mouse.get_pos())  # Draw the image at the mouse position

    frame_texture = surface_to_texture(display)
    frame_texture.use(0)  # Bind the texture to texture unit 0
    program['tex'] = 0  # Set the shader uniform to use texture unit 0
    render_object.render(mode=mgl.TRIANGLE_STRIP)  # Render the quad with the texture
    pg.display.flip()
    frame_texture.release()  # Release the texture after rendering

    game.clock.tick(120)  # Limit the frame rate to the clock's tick rate