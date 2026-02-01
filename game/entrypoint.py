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
        self.size = self.screen_width, self.screen_height = 960, 600
        self.init()
        self.screen = GameScreen(self)

    def init(self):
        pygame.init()
        self.display = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
        )
        if FULLSCREEN:
            pygame.display.toggle_fullscreen()
        self.clock = pygame.time.Clock()
        # pygame.time.set_timer(events.SCREEN_RESIZE_EVENT, 500)

        self.cards = [
            CardSprite(
                self,
                (
                    random.choice(["club", "diamond", "heart", "spade"]),
                    random.randint(1, 13),
                ),
                x=50,
                y=50,
                scaling=1
            )
        ]
        
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
        self.clock.tick(30)

    def on_render(self):
        fps = int(self.clock.get_fps())
        # fps = self.clock.get_fps()
        self.display.blit(self.fps_font.render(f"FPS: {fps}", 1, "#000000"), (5, 5))


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
            pygame.display.update()
            self.on_loop()

        self.on_cleanup()


def main():
    theApp = App()
    theApp.on_execute()


if __name__ == "__main__":
    main()
