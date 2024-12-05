import pyxel
import variables_globales as vg

class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def activar(self, pacman):
        if abs(self.x - pacman.x) < pacman.tamano_colision * 2 and abs(self.y - pacman.y) < pacman.tamano_colision * 2:
            pacman.poder = True
            pacman.poder_tiempo = 600
            pacman.velocidad = 2
            return True
        return False

    def draw(self):
        pyxel.blt(self.x - 4, self.y - 4, 2, 4, 4, 8, 8, pyxel.COLOR_GRAY)