import pygame
import random
from .sprites.card import CardSprite
from .game import GameScreen
from . import event_definitions as events

FULLSCREEN = False


class App:
    def __init__(self):
        self._running = True
        self.display = None
        self.size = self.screen_width, self.screen_height = 1200, 900
        self.init()
        self.screen = GameScreen(self, ['Player 1', 'Player 2', 'Player 3', 'Player 4'])

    def init(self):
        pygame.init()
        self.display = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
        )
        if FULLSCREEN:
            pygame.display.toggle_fullscreen()
        self.clock = pygame.time.Clock()
        # pygame.time.set_timer(events.SCREEN_RESIZE_EVENT, 500)
        
        self.fps_font = pygame.font.SysFont(pygame.font.get_default_font(), 24)
        
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            print("Bye!")
            self._running = False
        
        if event.type == pygame.VIDEORESIZE:
            self.size = self.screen_width, self.screen_height = pygame.display.get_window_size()
            print(f"Window Resized! {self.size}")

    def on_loop(self):
        self.clock.tick(999)

    def on_render(self):
        fps = int(self.clock.get_fps())
        # fps = self.clock.get_fps()
        self.display.blit(self.fps_font.render(f"{fps}", 1, "#000000"), (5, 5))


    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.init()

        while self._running:
            events = pygame.event.get()
            for event in events:
                self.on_event(event)
            self.screen.loop(events)
            self.on_render()
            pygame.display.flip()
            self.on_loop()

        self.on_cleanup()


def main():
    theApp = App()
    theApp.on_execute()


if __name__ == "__main__":
    main()
