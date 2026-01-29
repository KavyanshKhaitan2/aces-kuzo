import pyglet
from pyglet.window import mouse
from .title_screen import TitleScreen

window = pyglet.window.Window()

bg_color = (224, 230, 237)

pyglet.gl.glClearColor(bg_color[0] / 255, bg_color[1] / 255, bg_color[2] / 255, 1.0)

fps_display = pyglet.window.FPSDisplay(window=window, samples=1)
fps_display.label.font_size = 16
fps_display.label.anchor_y = "top"

current_screen = None


def set_current_screen(screen):
    global current_screen
    if current_screen:
        current_screen.deinit()
    current_screen = screen


@window.event
def on_draw():
    window.clear()
    current_screen.draw()
    fps_display.draw()


@window.event
def on_key_press(symbol, modifiers):
    print(f"A key was pressed {symbol=}, {modifiers=}")


@window.event
def on_mouse_press(x, y, button, modifiers):
    current_screen.mouse_press(x, y, button, modifiers)


@window.event
def on_resize(w, h):
    fps_display.label.y = window.height - 10
    current_screen.resize(w, h)


def main():
    set_current_screen(TitleScreen(set_current_screen, window=window))
    pyglet.app.run()
