import pyxel
from fantasma import Fantasma

class Blinky(Fantasma):
    def __init__(self):
        super().__init__(1, "arriba", 200, 140, 1, 0, 32, 16, 16, pyxel.COLOR_GRAY)