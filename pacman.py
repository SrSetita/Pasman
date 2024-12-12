import pyxel
import random
class Pacman:
    def __init__(self, velocidad: int, poder: bool, x, y):
        self.velocidad = velocidad
        self.poder = poder
        self.direccion = "arriba"
        self.x = x
        self.y = y
        self.tamaño_colision = 8  # Tamaño de colisión (radio de Pac-Man)
        self.poder = False  # Si Pacman tiene poder
        self.poder_tiempo = 0  # Temporizador del poder
    
    def centrar_en_celda(self):
        self.x = (self.x // 20) * 20 + 10
        self.y = (self.y // 20) * 20 + 10


    def mover(self, paredes):
        nueva_x, nueva_y = self.x, self.y

        self.centrar_en_celda()

        if self.direccion == "arriba":
            nueva_y -= self.velocidad
        elif self.direccion == "abajo":
            nueva_y += self.velocidad
        elif self.direccion == "izquierda":
            nueva_x -= self.velocidad
        elif self.direccion == "derecha":
            nueva_x += self.velocidad


        # Verificar si la nueva posición colisiona con alguna pared
        for pared in paredes:
            if pared.detectar_colision_en_posicion(nueva_x, nueva_y, self.tamaño_colision):
                return  # No mover si hay colisión con una pared

        #teletransporte si borde
        if nueva_x < 0:
            nueva_x = 440 - 20
        elif nueva_x > 440:
            nueva_x = 0 + 20

        if nueva_y < 0:
            nueva_y = 390 - 20 - 10
        elif nueva_y > 390 - 10:
            nueva_y = 0 + 20

        # Si no hay colisión, actualizamos la posición
        self.x, self.y = nueva_x, nueva_y

    def input_direccion(self):
        if pyxel.btn(pyxel.KEY_W):  
            self.direccion = "arriba"
        elif pyxel.btn(pyxel.KEY_S):  
            self.direccion = "abajo"
        elif pyxel.btn(pyxel.KEY_A):  
            self.direccion = "izquierda"
        elif pyxel.btn(pyxel.KEY_D):  
            self.direccion = "derecha"

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.x, self.y, self.tamaño_colision, pyxel.COLOR_YELLOW)
        if self.direccion == "derecha":
            pyxel.tri(self.x, self.y, self.x + 8, self.y - 4, self.x + 8, self.y + 4, 0)
        elif self.direccion == "abajo":
            pyxel.tri(self.x, self.y, self.x - 4, self.y + 8, self.x + 4, self.y + 8, 0)
        elif self.direccion == "izquierda":
            pyxel.tri(self.x, self.y, self.x - 8, self.y - 4, self.x - 8, self.y + 4, 0)
        elif self.direccion == "arriba":
            pyxel.tri(self.x, self.y, self.x - 4, self.y - 8, self.x + 4, self.y - 8, 0)

    def activar_poder(self):
        if self.poder:
            self.poder_tiempo -= 1  # Decrementar el temporizador de poder
        if self.poder_tiempo <= 0:  # Desactivar poder cuando el tiempo se agote
            self.poder = False
            self.velocidad = 2  # Restaurar la velocidad normal
