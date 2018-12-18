import pyglet

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()