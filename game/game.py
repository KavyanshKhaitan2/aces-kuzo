import pygame
import random
from .sprites.card import CardSprite
from .sprites.card_deck import CardDeck
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
            ) for _ in range(6)
        ]
        self.card_deck = CardDeck(self, self.cards)

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

        self.card_deck.draw(events)

    def on_cleanup(self):
        pygame.quit()

    def loop(self, events):
        for event in events:
            self.on_event(event)
        self.on_loop()
        self.on_render(events)
