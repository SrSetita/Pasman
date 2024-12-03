import pyxel
import random
class Pared:
    def __init__(self, posicionX: int, posicionY: int, ancho: int, alto: int):
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.ancho = ancho
        self.alto = alto

    def detectar_colision_en_posicion(self, nueva_x, nueva_y, tamano_colision):
        if (self.posicionX < nueva_x + tamano_colision and 
            nueva_x - tamano_colision < self.posicionX + self.ancho and 
            self.posicionY < nueva_y + tamano_colision and 
            nueva_y - tamano_colision < self.posicionY + self.alto):
            return True
        return False

    def draw(self):
        pyxel.blt(self.posicionX, self.posicionY,0,0,0, self.ancho, self.alto, pyxel.COLOR_GRAY)
