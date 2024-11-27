import pyxel
import random

class Pacman:
    def __init__(self, velocidad: int, poder: bool, x, y):
        self.velocidad = velocidad
        self.poder = poder
        self.direccion = "derecha"
        self.vidas = 3
        self.x = x
        self.y = y
        self.tamano_colision = 8  # Tamaño de colisión (radio de Pac-Man)

    def mover(self, paredes):
        nueva_x, nueva_y = self.x, self.y

        if self.direccion == "arriba":
            nueva_y -= self.velocidad
        elif self.direccion == "abajo":
            nueva_y += self.velocidad
        elif self.direccion == "izquierda":
            nueva_x -= self.velocidad
        elif self.direccion == "derecha":
            nueva_x += self.velocidad

        # Verificar colisiones con los bordes de la pantalla
        if nueva_x < 0 or nueva_x > pyxel.width - self.tamano_colision * 2 or nueva_y < 0 or nueva_y > pyxel.height - self.tamano_colision * 2:
            return  # No mover si está fuera de los límites de la pantalla

        # Verificar si la nueva posición colisiona con alguna pared
        for pared in paredes:
            if pared.detectar_colision_en_posicion(nueva_x, nueva_y, self.tamano_colision):
                return  # No mover si hay colisión con una pared

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
        pyxel.circ(self.x, self.y, self.tamano_colision, pyxel.COLOR_YELLOW)
        if self.direccion == "derecha":
            pyxel.tri(self.x, self.y, self.x + 8, self.y - 4, self.x + 8, self.y + 4, 0)
        elif self.direccion == "abajo":
            pyxel.tri(self.x, self.y, self.x - 4, self.y + 8, self.x + 4, self.y + 8, 0)
        elif self.direccion == "izquierda":
            pyxel.tri(self.x, self.y, self.x - 8, self.y - 4, self.x - 8, self.y + 4, 0)
        elif self.direccion == "arriba":
            pyxel.tri(self.x, self.y, self.x - 4, self.y - 8, self.x + 4, self.y - 8, 0)


class Pared:
    def __init__(self, posicionX: int, posicionY: int, ancho: int, alto: int):
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.ancho = ancho
        self.alto = alto

    def detectar_colision_en_posicion(self, nueva_x, nueva_y, tamano_colision):
        # Modificado para tomar en cuenta el tamaño de colisión
        if (self.posicionX < nueva_x + tamano_colision and 
            nueva_x - tamano_colision < self.posicionX + self.ancho and 
            self.posicionY < nueva_y + tamano_colision and 
            nueva_y - tamano_colision < self.posicionY + self.alto):
            return True
        return False

    def draw(self):
        pyxel.rect(self.posicionX, self.posicionY, self.ancho, self.alto, pyxel.COLOR_GRAY)


class Fantasma:
    def __init__(self, velocidad: int, direccion, x, y):
        self.velocidad = velocidad
        self.direccion = direccion
        self.x = x
        self.y = y
        self.punto_inicio = (x, y)  # Guardar el punto de inicio

    def mover(self, paredes):
        nueva_x, nueva_y = self.x, self.y

        if self.direccion == "arriba":
            nueva_y -= self.velocidad
        elif self.direccion == "abajo":
            nueva_y += self.velocidad
        elif self.direccion == "izquierda":
            nueva_x -= self.velocidad
        elif self.direccion == "derecha":
            nueva_x += self.velocidad

        # Verificar colisiones con los bordes de la pantalla
        if nueva_x < 0 or nueva_x > pyxel.width - 8 or nueva_y < 0 or nueva_y > pyxel.height - 8:
            self.cambiar_direccion()
            return

        # Verificar colisiones con las paredes
        colision = False
        for pared in paredes:
            if pared.detectar_colision_en_posicion(nueva_x, nueva_y, 8):  # Los fantasmas tienen un tamaño de colisión de 8
                colision = True
                break

        if colision:
            self.cambiar_direccion()
        else:
            self.x, self.y = nueva_x, nueva_y

    def cambiar_direccion(self):
        direcciones = ["arriba", "abajo", "izquierda", "derecha"]
        self.direccion = random.choice(direcciones)

    def draw(self):
        pyxel.rect(self.x, self.y, 8, 8, pyxel.COLOR_RED)

    def colision_con_pacman(self, pacman):
        if abs(self.x - pacman.x) < pacman.tamano_colision * 2 and abs(self.y - pacman.y) < pacman.tamano_colision * 2:
            return True
        return False

    def reset(self):
        self.x, self.y = self.punto_inicio


class Consumible:
    def __init__(self, tipo: str, x, y):
        self.tipo = tipo
        self.x = x
        self.y = y

    def activar(self, pacman):
        if pacman.x == self.x and pacman.y == self.y:
            if self.tipo == "fruta":
                pacman.vidas += 1
            elif self.tipo == "pildora":
                pacman.poder = True
            return True
        return False

    def draw(self):
        if self.tipo == "fruta":
            pyxel.circ(self.x, self.y, 4, pyxel.COLOR_GREEN)
        elif self.tipo == "pildora":
            pyxel.rect(self.x - 2, self.y - 2, 4, 4, pyxel.COLOR_NAVY)
        elif self.tipo == "puntos":
            pyxel.rect(self.x - 1, self.y - 1, 2, 2, pyxel.COLOR_WHITE)


def update():
    pacman.input_direccion()
    pacman.mover(paredes)

    for fantasma in fantasmas:
        if fantasma.colision_con_pacman(pacman):
            pacman.vidas -= 1
            pacman.x = 160
            pacman.y = 120
            for fantasma in fantasmas:
                fantasma.reset()

    for fantasma in fantasmas:
        fantasma.mover(paredes)

    for consumible in consumibles:
        if consumible.activar(pacman):
            consumibles.remove(consumible)

def draw():
    pacman.draw()
    for fantasma in fantasmas:
        fantasma.draw()
    for consumible in consumibles:
        consumible.draw()
    for pared in paredes:
        pared.draw()


pyxel.init(320, 240, title="Pacman Game", fps=60)

pacman = Pacman(2, False, 160, 120)
fantasmas = [Fantasma(1, "arriba", 40, 40), Fantasma(1, "abajo", 280, 200)]
consumibles = [Consumible("fruta", 80, 80), Consumible("pildora", 240, 200), Consumible("puntos", 160, 100)]

paredes = [
    # Bordes del mapa
    Pared(0, 0, 320, 5), Pared(0, 0, 5, 240), Pared(315, 0, 5, 240), Pared(0, 235, 320, 5),
    
    # Área de los fantasmas en el centro
    Pared(100, 100, 55, 5), Pared(170, 100, 55, 5), Pared(100, 140, 125, 5), Pared(100, 100, 5, 45), Pared(220, 100, 5, 45),

    # Paredes internas
    Pared(100, 80, 125, 5), Pared(100, 60, 125, 5), Pared(100, 160, 125, 5),
]

pyxel.run(update, draw)
