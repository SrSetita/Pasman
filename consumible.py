import pyxel
import random
import variables_globales as vg
class Consumible:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo

    def activar(self, pacman):
        # Verificar si Pacman está en la misma posición que el consumible
        if abs(self.x - pacman.x) < pacman.tamano_colision * 2 and abs(self.y - pacman.y) < pacman.tamano_colision * 2:
            if self.tipo == 2:  # Punto
                vg.puntospacman += 1
                vg.puntosmapa += 1
            elif self.tipo == 3:  # Power-up
                pacman.poder = True
                pacman.poder_tiempo = 600  # Duración del poder (en segundos)
                pacman.velocidad = 2  # Aumentar la velocidad de Pacman
            elif self.tipo == 4:  # Fruta
                vg.puntospacman += 5
                vg.vidaspacman += 1
            return True  # Consumible activado
        return False  # No activado

    def draw(self):
        if self.tipo == 2:  # Punto
            pyxel.rect(self.x - 1, self.y - 1, 3, 3, pyxel.COLOR_WHITE)  # Dibuja el punto
        elif self.tipo == 3:  # Power-up
            pyxel.blt(self.x - 4, self.y - 4, 2, 4, 4, 8, 8, pyxel.COLOR_GRAY)  # Dibuja el power-up
        elif self.tipo == 4:  # Fruta
            pyxel.blt(self.x - 4, self.y - 4, 2, 20, 2, 15, 15, pyxel.COLOR_GRAY)  # Dibuja la fruta
