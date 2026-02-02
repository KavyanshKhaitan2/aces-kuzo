import pygame
from typing import Literal
from .. import assets
from .card import CardSprite
from functools import partial

CARD_NAMES = {
    1: "A",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
}


class CardDeck:
    def __init__(self, master, cards: list[CardSprite], x=None, y=None, scaling=None, onclick=None):
        self._scaling = 1
        self._onclick = None
        
        self.onclick = onclick
        
        self.master = master
        self.x, self.y = x, y
        self.cards = cards
        if len(cards) != 6:
            raise NotImplementedError("More or less than 6 cards not implemented!!!")
        if scaling is None:
            scaling = self.cards[0].scaling
        self.scaling = scaling
        for card in self.cards:
            card.scaling = scaling

        rect_width, rect_height = ((self.cards[0].width + (10 * self.scaling)) * 3) + (10 * self.scaling), (
            (self.cards[0].height + (10 * self.scaling)) * 2
        ) + (10 * self.scaling)

        if x is None:
            rect_x = self.master.screen_width - rect_width - (10 * self.scaling)
        if y is None:
            rect_y = self.master.screen_height - rect_height - (10 * self.scaling)

        self.rect = pygame.rect.Rect(rect_x, rect_y, rect_width, rect_height)

    def draw(self, events=None, x=None, y=None, scaling=None):
        rect_width, rect_height = ((self.cards[0].width + (10 * self.scaling)) * 3) + (10 * self.scaling), (
            (self.cards[0].height + (10 * self.scaling)) * 2
        ) + (10 * self.scaling)
        x = self.x if x is None else x
        y = self.y if y is None else y
        
        if x is None:
            rect_x = self.master.screen_width - rect_width - 10
        else:
            rect_x = x
        if y is None:
            rect_y = self.master.screen_height - rect_height - 10
        else:
            rect_y = y

        self.rect = pygame.rect.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(
            self.master.display,
            "#33618F",
            self.rect,
            0,
            10,
        )

        for i, card in enumerate(self.cards):
            x = i % 3
            y = 1 if i > 2 else 0
            card.draw(
                events,
                self.rect.x + (10 * self.scaling) + ((self.cards[0].width + (10 * self.scaling)) * x),
                self.rect.y + (10 * self.scaling) + ((self.cards[0].height + (10 * self.scaling)) * y),
                scaling=scaling,
            )

    def colliding(self, x, y=None):
        if y is None:
            x, y = x
        return self.rect.collidepoint(x, y)

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    @property
    def size(self):
        return self.rect.size

    @property
    def scaling(self):
        return self._scaling
    
    @scaling.setter
    def scaling(self, value):
        if self._scaling == value:
            return
        self._scaling = value
        for card in self.cards:
            card.scaling = value
            card.load_image()
    
    @property
    def onclick(self):
        return self._onclick
    
    @onclick.setter
    def onclick(self, callable):
        if self._onclick == callable:
            return
        self._onclick = callable
        for i, card in enumerate(self.cards):
            if callable is not None:
                card.onclick = partial(callable, i)
            else:
                card.onclick = None