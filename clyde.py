import pyxel
from fantasma import Fantasma

class Clyde(Fantasma):
    def __init__(self):
        super().__init__(2, "derecha", 200, 140, 1, 0, 96, 16, 16, pyxel.COLOR_GRAY)