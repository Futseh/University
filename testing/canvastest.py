import pyglet
from pyglet.gl import *

win = pyglet.window.Window()

@win.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)

    glEnd()

pyglet.app.run()