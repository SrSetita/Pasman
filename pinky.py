import pyxel
from fantasma import Fantasma

class Pinky(Fantasma):
    def __init__(self):
        super().__init__(1.5, "derecha", 200, 140, 1, 0, 64, 16, 16, pyxel.COLOR_GRAY)