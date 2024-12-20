import pyxel
import random
import variables_globales as vg
class Pared:
    def __init__(self, posicionX: int, posicionY: int, ancho: int, alto: int):
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.ancho = ancho
        self.alto = alto

    def detectar_colision_en_posicion(self, nueva_x, nueva_y, tamaño_colision):
        if (self.posicionX < nueva_x + tamaño_colision and 
            nueva_x - tamaño_colision < self.posicionX + self.ancho and 
            self.posicionY < nueva_y + tamaño_colision and 
            nueva_y - tamaño_colision < self.posicionY + self.alto):
            return True
        return False

    def draw(self):
        if vg.puntosmapa < 194:
            pyxel.blt(self.posicionX, self.posicionY,0,0,0, self.ancho, self.alto, pyxel.COLOR_GRAY)
        if vg.puntosmapa >= 194 and vg.puntosmapa< 391:
            pyxel.blt(self.posicionX, self.posicionY,0,21,21, self.ancho, self.alto, pyxel.COLOR_GRAY)
        if vg.puntosmapa >= 391:
            pyxel.blt(self.posicionX, self.posicionY,0,0,21, self.ancho, self.alto, pyxel.COLOR_GRAY)
