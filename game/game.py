import pygame
import random
from .sprites.card import CardSprite, CARD_NAMES
from .sprites.card_deck import CardDeck
from functools import partial
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .entrypoint import App
else:
    App = None

ALL_CARDS = []

for i in range(1, 14):
    ALL_CARDS.append(("club", i))
    ALL_CARDS.append(("diamond", i))
    ALL_CARDS.append(("heart", i))
    ALL_CARDS.append(("spade", i))


class GameScreen:
    def __init__(self, master: App, player_names: list[str]):
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 32)

        self.master = master
        self.display = master.display
        self.clock = master.clock
        self._running = True
        self.display = self.master.display
        self.size = self.screen_width, self.screen_height = self.master.size

        self.player_names = player_names

        self.init()

    def init(self):
        self.cards_in_pickup_pile = ALL_CARDS.copy()
        # self.pickup_pile_sprite = 
        random.shuffle(self.cards_in_pickup_pile)
        self.card_decks: list[CardDeck] = []
        for i in range(len(self.player_names)):
            card_sprites = []
            for _ in range(6):
                card_sprites.append(
                    CardSprite(
                        self,
                        self.cards_in_pickup_pile.pop(),
                        x=50,
                        y=50,
                        scaling=1,
                    )
                )

            deck = CardDeck(self, card_sprites, scaling=1 if i == 0 else 0.5)
            self.card_decks.append(deck)
            deck.onclick = lambda x, i=i: print(f"DECK {i}: Card {x}")
        self.relocate_decks()
        print(self.cards_in_pickup_pile)

    def relocate_decks(self):
        for i, deck in enumerate(self.card_decks):
            if i == 0:
                deck.x = (self.screen_width - deck.width) / 2
                deck.y = self.screen_height - deck.height - 5
            if i == 1:
                deck.x = 5
                deck.y = (self.screen_height - deck.height) / 2
            if i == 2:
                deck.x = (self.screen_width - deck.width) / 2
                deck.y = 5
            if i == 3:
                deck.x = self.screen_width - deck.width - 5
                deck.y = (self.screen_height - deck.height) / 2

    def on_event(self, event):
        if event.type == pygame.VIDEORESIZE:
            self.size = self.screen_width, self.screen_height = self.master.size
            self.relocate_decks()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("mouse clicked!", pygame.mouse.get_pos())

    def on_loop(self): ...

    def on_render(self, events):
        self.display.fill("#3F7CB6")

        for deck in reversed(self.card_decks):
            deck.draw(events)

        text = self.font.render(self.player_names[0], True, "#000000")
        text_x = self.card_decks[0].x + (
            (self.card_decks[0].width - text.get_width()) / 2
        )
        text_y = self.card_decks[0].y - text.get_height()
        self.display.blit(text, (text_x, text_y))

    def on_cleanup(self):
        pygame.quit()

    def loop(self, events):
        for event in events:
            self.on_event(event)
        self.on_loop()
        self.on_render(events)
