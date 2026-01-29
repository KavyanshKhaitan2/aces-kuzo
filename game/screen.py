import pyglet

class Screen:
    def __init__(self, set_current_screen, window:pyglet.window.BaseWindow):
        self.set_current_screen = set_current_screen
        self.window = window
        self.batch = pyglet.graphics.Batch()
        self.init()
        self.resize(window.width, window.height)

    def draw(self):
        self.batch.draw()
    
    def init(self):
        ...
    
    def mouse_press(self, x, y, button, modifiers):
        ...
    
    def resize(self, w, h):
        ...
    
    def deinit(self):
        ...