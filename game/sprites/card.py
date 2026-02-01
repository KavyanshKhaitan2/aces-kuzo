import pygame
from typing import Literal
from .. import assets

CARD_NAMES = {
    1: 'A',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'J',
    12: 'Q',
    13: 'K'
}

class CardSprite:
    def __init__(self, master, card:tuple[Literal['club', 'diamond', 'heart', 'spade'], Literal[1,2,3,4,5,6,7,8,9,10,11,12,13]], x, y, scaling=1):
        self.master = master
        self.card = card
        self.filepath = f'assets/boardgamepack/PNG/Cards/card{card[0].title()}s{CARD_NAMES[card[1]]}.png'
        self.scaling = scaling
        self.image = pygame.image.load(self.filepath)
        self.image = pygame.transform.smoothscale(self.image, [x*scaling for x in self.image.get_size()])
        self.x, self.y = x, y
    
    def draw(self, events, x=None, y=None, scaling=None):
        self.x = self.x if x is None else x
        self.y = self.y if y is None else y
        
        scaling = self.scaling if scaling is None else scaling
        
        if scaling != self.scaling:
            self.scaling = scaling
            self.image = pygame.image.load(self.filepath)
            self.image = pygame.transform.smoothscale(self.image, [x*scaling for x in self.image.get_size()])
        
        self.master.display.blit(self.image, (self.x, self.y))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.colliding(pygame.mouse.get_pos()):
                    assets.SOUND_CARD_CLICKED.play()
                    print(f"card {self.card[0]}{self.card[1]}: click!")
    
    def colliding(self, x, y=None):
        if y is None:
            x, y = x
        x = x - self.x
        y = y - self.y
        return self.image.get_rect().collidepoint(x, y)
    
    @property
    def width(self):
        return self.image.get_width()
    
    @property
    def height(self):
        return self.image.get_height()
    
    @property
    def size(self):
        return self.width, self.height