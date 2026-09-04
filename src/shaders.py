import array
import moderngl as mgl


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
    f_color = vec4(texture(tex, uvs).r, texture(tex, uvs).g, texture(tex, uvs).b, 1.0);
}
'''

