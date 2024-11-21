import pyxel

class Pacman:
    def __init__ (self, velocidad: int, poder: bool, x,  y):
        self.velocidad = velocidad #velocidad que tiene el pacman
        self.poder = poder #si pacman esta transformado o no
        self.direccion = "derecha" #hacia donde mira el pacman, esta es la inicial
        self.vidas = 3
        self.x = x
        self.y = y
        
    def input_direccion(self): #funcion que mueve el pacman usando WASD

        if pyxel.btn(pyxel.KEY_W):  # mover arriba
            self.direccion = "arriba"
            self.y -= 2
        elif pyxel.btn(pyxel.KEY_S):  # mover abajo
            self.direccion = "abajo"
            self.y += 2
        elif pyxel.btn(pyxel.KEY_A):  # Move left
            self.direccion = "izquierda"
            self.x -= 2
        elif pyxel.btn(pyxel.KEY_D):  # Move derecha
            self.direccion = "derecha"
            self.x += 2

    

class Fantasma:
    def __init__ (self, velocidad: int, direccion):
        self.velocidad = velocidad #velocidad que tiene el fantasma
        self.direccion = direccion #hacia donde mira el fantasma

class Consumible:
     def __init__ (self, tipo: str):
         self.tipo = tipo #Nos dice que tipo de cosa se come el pacman: "fruta, pildora o puntos"

class Pared:
    def __init__ (self, posicionX: int, posicionY: int, choque: bool):
        self.posicionX = posicionX #posición en X de la pared
        self.posicionY = posicionY #posición en Y de la pared
        self.choque = choque #dice si un fantasma o pacman estas tocando la pared