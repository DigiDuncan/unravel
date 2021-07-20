import nygame
import pygame


class Game(nygame.Game):
    def __init__(self):
        super().__init__(size = (1280, 720), fps = 120, showfps = True, bgcolor=0xA0A0A0)

    def loop(self, events):
        pass


def main():
    Game().run()


# This is needed, or else calling `python -m <name>` will mean that main() is called twice.
if __name__ == "__main__":
    main()
