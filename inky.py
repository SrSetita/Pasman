import pyxel
from fantasma import Fantasma

class Inky(Fantasma):
    def __init__(self):
        super().__init__(0.5, "izquierda", 200, 140, 1, 0, 0, 16, 16, pyxel.COLOR_GRAY)