import pyxel
import random

class Pacman:
    def __init__(self, velocidad: int, poder: bool, x, y):
        self.velocidad = velocidad
        self.poder = poder
        self.direccion = "arriba"
        self.vidas = 3
        self.puntos = 0
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
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def activar(self, pacman):
        if abs(self.x - pacman.x) < pacman.tamano_colision * 2 and abs(self.y - pacman.y) < pacman.tamano_colision * 2:
            pacman.puntos += 1
            return True
        return False

    def draw(self):
        pyxel.rect(self.x - 1, self.y - 1, 2, 2, pyxel.COLOR_WHITE)


def posicion_libre(x, y, paredes, consumibles):
    # Verificar si la posición no está ocupada por una pared
    for pared in paredes:
        if pared.detectar_colision_en_posicion(x, y, 4):
            return False

    # Verificar si la posición no está ocupada por otro consumible
    for consumible in consumibles:
        if abs(consumible.x - x) < 4 and abs(consumible.y - y) < 4:
            return False

    return True


def generar_puntos(paredes, cantidad, consumibles):
    puntos = []
    while len(puntos) < cantidad:
        x = random.randint(0, pyxel.width - 1)
        y = random.randint(0, pyxel.height - 1)

        if posicion_libre(x, y, paredes, consumibles):
            puntos.append(Consumible(x, y))
    return puntos


def update():
    pacman.input_direccion()
    pacman.mover(paredes)

    # Verificar si Pacman colisiona con algún fantasma
    for fantasma in fantasmas:
        if fantasma.colision_con_pacman(pacman):
            pacman.vidas -= 1
            pacman.x = 167
            pacman.y = 135
            for fantasma in fantasmas:
                fantasma.reset()

    # Mover fantasmas
    for fantasma in fantasmas:
        fantasma.mover(paredes)

    # Verificar si Pacman activa algún consumible
    for consumible in consumibles[:]:  # Iteramos sobre una copia de la lista para poder eliminar elementos
        if consumible.activar(pacman):
            consumibles.remove(consumible)  # Eliminar el consumible recolectado


def draw():
    pacman.draw()
    for fantasma in fantasmas:
        fantasma.draw()
    for consumible in consumibles:
        consumible.draw()
    for pared in paredes:
        pared.draw()

    # Mostrar los puntos recolectados
    pyxel.text(5, 5, f"Puntos: {pacman.puntos}", pyxel.COLOR_WHITE)


# Inicialización del juego
pyxel.init(325, 250, title="Pacman Game", fps=60)

pacman = Pacman(2, False, 167, 135)
fantasmas = [Fantasma(1, "arriba", 40, 40), Fantasma(1, "abajo", 280, 200)]

paredes = [
    # Bordes del mapa
    Pared(0, 0, 325, 5), Pared(0, 0, 5, 250), Pared(320, 0, 5, 250), Pared(0, 245, 325, 5),
    # Área de los fantasmas en el centro
    Pared(110, 110, 48, 5), Pared(175, 110, 50, 5), Pared(153, 150, 26, 5), Pared(153, 110, 5, 45), Pared(175, 110, 5, 45),
    # Paredes internas
    Pared(25, 85, 270, 5), Pared(110, 60, 115, 5), Pared(110, 175, 115, 5), Pared(25, 85, 5, 95), Pared(295, 85, 5, 95),
    Pared(220, 110, 5, 45), Pared(110, 110, 5, 45), Pared(245, 110, 5, 45), Pared(270, 110, 5, 45), Pared(85, 110, 5, 45),
    Pared(57.5, 110, 5, 45),
]

# Generar puntos al inicio
consumibles = generar_puntos(paredes, 100, [])

pyxel.run(update, draw)