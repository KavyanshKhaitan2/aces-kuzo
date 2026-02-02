import pygame
from typing import Literal
from .. import assets

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


class CardSprite:
    def __init__(
        self,
        master,
        card: tuple[
            Literal["club", "diamond", "heart", "spade"],
            Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        ],
        x,
        y,
        scaling=1,
        onclick=None,
    ):
        self.master = master
        self.card = card
        self.current_rendered_scaling = self.scaling = scaling
        self.showing = self.current_rendered_showing = True
        self.x, self.y = x, y
        self.onclick = onclick

        self.card_back_image = "assets/boardgamepack/PNG/Cards/cardBack_green5.png"

        self.load_image(force=True)

    def draw(self, events=None, x=None, y=None, scaling=None):
        self.x = self.x if x is None else x
        self.y = self.y if y is None else y

        scaling = self.scaling if scaling is None else scaling

        self.scaling = scaling
        self.load_image()

        self.load_image()

        self.master.display.blit(self.image, (self.x, self.y))

        if events is None:
            return
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.colliding(pygame.mouse.get_pos()):
                    assets.SOUND_CARD_CLICKED.play()
                    print(f"card {self.card[0]}{self.card[1]}: click!")
                    if self.onclick:
                        self.onclick()
                    self.showing = not self.showing

    def colliding(self, x, y=None):
        if y is None:
            x, y = x
        x = x - self.x
        y = y - self.y
        return self.image.get_rect().collidepoint(x, y)

    def load_image(self, force=False):
        if (
            (self.showing == self.current_rendered_showing)
            and (self.scaling == self.current_rendered_scaling)
            and not force
        ):
            return
        self.current_rendered_showing = self.showing
        self.current_rendered_scaling = self.scaling
        
        if self.showing:
            self.filepath = f"assets/boardgamepack/PNG/Cards/card{self.card[0].title()}s{CARD_NAMES[self.card[1]]}.png"
        else:
            self.filepath = self.card_back_image
        self.image = pygame.image.load(self.filepath).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image, [x * self.scaling for x in self.image.get_size()]
        )

    @property
    def width(self):
        return self.image.get_width()

    @property
    def height(self):
        return self.image.get_height()

    @property
    def size(self):
        return self.width, self.height
