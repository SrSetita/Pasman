import pyxel
from fantasma import Fantasma

class Pinky(Fantasma):
    def __init__(self):
        super().__init__(1.25, "arriba", 200, 140, 1, 0, 64, 16, 16, 600, 35, pyxel.COLOR_GRAY)

    