import pygame
import random
from .sprites.card import CardSprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .entrypoint import App
else:
    App = None


class GameScreen:
    def __init__(self, master: App):
        self.master = master
        self.display = master.display
        self.clock = master.clock
        self._running = True
        self.display = self.master.display
        self.size = self.screen_width, self.screen_height = self.master.size
        self.init()

    def init(self):
        self.cards = [
            CardSprite(
                self,
                (
                    random.choice(["club", "diamond", "heart", "spade"]),
                    random.randint(1, 13),
                ),
                x=50,
                y=50,
                scaling=1,
            )
        ]

    def on_event(self, event):
        if event.type == pygame.VIDEORESIZE:
            self.size = self.screen_width, self.screen_height = self.master.size
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse clicked!", pygame.mouse.get_pos())

    def on_loop(self):
        ...
        
    def on_render(self, events):
        mouse_pos = pygame.mouse.get_pos()

        self.display.fill("#3F7CB6")

        rect_width, rect_height = ((self.cards[0].width + 10) * 3) + 10, ((self.cards[0].height + 10) * 2) + 10
        rect_x = self.screen_width - rect_width - 10
        rect_y = self.screen_height - rect_height - 10
        pygame.draw.rect(
            self.display,
            "#33618F",
            pygame.rect.Rect(
                rect_x,
                rect_y,
                rect_width,
                rect_height
            ),
            0,
            10,
        )

        for card in self.cards:
            card.draw(events)

    def on_cleanup(self):
        pygame.quit()

    def loop(self, events):
        for event in events:
            self.on_event(event)
        self.on_loop()
        self.on_render(events)
