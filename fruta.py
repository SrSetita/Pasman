import pyxel
import variables_globales as vg
import random

class Fruta:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.toca = random.randint(0,10)
    def activar(self, pacman):
        if self.toca <= 3:
            if abs(self.x - pacman.x) < pacman.tamaño_colision * 2 and abs(self.y - pacman.y) < pacman.tamaño_colision * 2:
                vg.puntospacman += 5
                vg.vidaspacman += 1
                return True
            return False
        else:
            if abs(self.x - pacman.x) < pacman.tamaño_colision * 2 and abs(self.y - pacman.y) < pacman.tamaño_colision * 2:
                vg.puntospacman += 0
                vg.vidaspacman += 0
                return True
            return False

    def draw(self):
        if self.toca <= 3:
            pyxel.blt(self.x - 4, self.y - 4, 2, 20, 2, 15, 15, pyxel.COLOR_GRAY)
        else:
            pyxel.blt(self.x - 4, self.y - 4, 2, 50, 50, 15, 15, pyxel.COLOR_RED)