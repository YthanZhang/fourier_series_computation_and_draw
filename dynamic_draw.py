import pyglet
import sys
import scipy

width, height = 1920, 1080
window = pyglet.window.Window(width, height, fullscreen=True)
label = pyglet.text.Label("Hello world",
                          font_name="Time New Roman",
                          font_size=36,
                          x=20, y=window.height - 20,
                          anchor_x='left', anchor_y='top')

group0 = pyglet.graphics.OrderedGroup(0)
group1 = pyglet.graphics.OrderedGroup(1)
group2 = pyglet.graphics.OrderedGroup(2)
batch = pyglet.graphics.Batch()
background = pyglet.shapes.Rectangle(0, 0, width, height, color=(80, 80, 145),
                                     batch=batch,
                                     group=group0)

arrow_img = pyglet.image.load("img/arrow.png")
arrow_img.anchor_y = arrow_img.height // 2
arrow1 = pyglet.sprite.Sprite(arrow_img, batch=batch, group=group2)
arrow1.scale = 0.1
arrow1.update(width // 2, height // 2)

rotation_per_sec = 360


def update(dt):
    print("update")

    arrow1.rotation += rotation_per_sec * dt

@window.event
def on_draw():
    print("draw")

    window.clear()
    batch.draw()
    label.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.F and modifiers & pyglet.window.key.MOD_SHIFT:
        pyglet.app.exit()
        sys.exit(0)
    elif symbol == pyglet.window.key.ESCAPE:
        pyglet.app.exit()
        sys.exit(0)
    else:
        pass


pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()

