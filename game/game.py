import pyglet
from .screen import Screen

play_button_image = pyglet.resource.image("assets/play_button.png")

up_button_image = pyglet.resource.image("assets/up_button.png")
down_button_image = pyglet.resource.image("assets/down_button.png")


class GameScreen(Screen):
    def init(self):
        self.play_game_button = pyglet.gui.PushButton(
            pressed=play_button_image,
            unpressed=play_button_image,
            batch=self.batch,
            x=1,
            y=1,
        )
        self.window.push_handlers(self.play_game_button)
        self.play_game_button.set_handler("on_press", self.play_button_pressed)
        # self.play_game_button.set_handler('on_release', my_on_release_handler)

        self.title_text = pyglet.text.Label(
            "Kuzo!",
            font_size=36,
            anchor_x="center",
            anchor_y="center",
            color=(0, 0, 0, 255),
            batch=self.batch,
        )

    def draw(self):
        self.batch.draw()

    def resize(self, w, h):
        self.title_text.position = (w // 2, h // 2 + 50, 0)
        self.play_game_button.position = (
            w // 2 - play_button_image.width // 2,
            h // 2 - 50 - play_button_image.height // 2,
        )
        return super().resize(w, h)

    def deinit(self):
        self.play_game_button.pop_handlers()
        return super().deinit()
