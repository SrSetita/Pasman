import pyxel
import variables_globales as vg

class Fruta:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def activar(self, pacman):
        if abs(self.x - pacman.x) < pacman.tamano_colision * 2 and abs(self.y - pacman.y) < pacman.tamano_colision * 2:
            vg.puntospacman += 5
            vg.vidaspacman += 1
            return True
        return False

    def draw(self):
        pyxel.blt(self.x - 4, self.y - 4, 2, 20, 2, 15, 15, pyxel.COLOR_GRAY)