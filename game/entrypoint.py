import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()
label = pyglet.text.Label(
    "Hello, world!",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)

image = pyglet.resource.image("image.png")

current_module = None

circle_positions = [
    
]

@window.event
def on_draw():
    window.clear()
    current_module.draw(window)
    label.draw()
    image.blit(0, 0)
    for x, y in circle_positions:
        pyglet.shapes.Circle(x, y, 5).draw()

@window.event
def on_key_press(symbol, modifiers):
    print(f'A key was pressed {symbol=}, {modifiers=}')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
    if button == mouse.RIGHT:
        print('The right mouse button was pressed.')
    circle_positions.append((x, y))

def main():
    global current_module
    from . import title_screen as current_module
    pyglet.app.run()
