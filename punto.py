import pyxel
import variables_globales as vg

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def activar(self, pacman):
        if abs(self.x - pacman.x) < pacman.tamaño_colision * 2 and abs(self.y - pacman.y) < pacman.tamaño_colision * 2:
            vg.puntospacman += 1
            vg.puntosmapa += 1
            return True
        return False

    def draw(self):
        pyxel.rect(self.x - 1, self.y - 1, 3, 3, pyxel.COLOR_WHITE)