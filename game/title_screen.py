import pyglet
from PIL import Image
from io import BytesIO
from .screen import Screen

play_button_image = pyglet.resource.image("assets/play_button.png")

up_button_image = pyglet.resource.image("assets/up_button.png")
down_button_image = pyglet.resource.image("assets/down_button.png")


class TitleScreen(Screen):
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

    def play_button_pressed(self, widget):
        print("[DEBUG] Starting game...")
        self.set_current_screen(
            PlayerCountSelectScreen(self.set_current_screen, window=self.window)
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


class PlayerCountSelectScreen(Screen):
    def init(self):
        self.player_count = 1

        self.title_text = pyglet.text.Label(
            "Select Player Count (2-4)",
            font_size=36,
            anchor_x="center",
            anchor_y="center",
            color=(0, 0, 0, 255),
            batch=self.batch,
        )

        self.down_button = pyglet.gui.PushButton(
            x=0,
            y=0,
            unpressed=down_button_image,
            pressed=down_button_image,
            batch=self.batch,
        )
        self.window.push_handlers(self.down_button)
        self.down_button.set_handler("on_press", self.player_count_down)

        self.player_count_label = pyglet.text.Label(
            anchor_x="center",
            anchor_y="center",
            text="Loading...",
            batch=self.batch,
            color=(0, 0, 0),
            font_size=20,
        )

        self.up_button = pyglet.gui.PushButton(
            x=0,
            y=0,
            unpressed=up_button_image,
            pressed=up_button_image,
            batch=self.batch,
        )
        self.window.push_handlers(self.up_button)
        self.window.clear
        self.up_button.set_handler("on_press", self.player_count_up)
        self.state = "player_count_select"
        self.player_count_up(self.up_button)

    def player_count_down(self, widget):
        self.player_count -= 1 if self.player_count > 2 else 0
        self.player_count_label.text = f"{self.player_count} players"

    def player_count_up(self, widget):
        self.player_count += 1 if self.player_count < 4 else 0
        self.player_count_label.text = f"{self.player_count} players"

    def resize(self, w, h):

        self.title_text.position = (w // 2, h // 2 + 200, 0)

        self.down_button.x = w // 2 - down_button_image.width // 2
        self.down_button.y = h // 2 - down_button_image.height - 100

        self.player_count_label.x = w // 2
        self.player_count_label.y = h // 2 - 50

        self.up_button.x = w // 2 - up_button_image.width // 2
        self.up_button.y = h // 2

        return super().resize(w, h)

    def draw(self):
        self.batch.draw()
