import pyxel
import variables_globales as vg
from punto import Punto
from power_up import PowerUp
from fruta import Fruta
class Consumible:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        if tipo == 2:
            self.consumible = Punto(x, y)
        elif tipo == 3:
            self.consumible = PowerUp(x, y)
        elif tipo == 4:
            self.consumible = Fruta(x, y)

    def activar(self, pacman):
        return self.consumible.activar(pacman)

    def draw(self):
        self.consumible.draw()