import pyxel

class Pacman:
    def __init__(self, velocidad: int, poder: bool, x, y):
        self.velocidad = velocidad
        self.poder = poder
        self.direccion = "derecha"
        self.vidas = 3
        self.x = x
        self.y = y

    def mover(self):
        if self.direccion == "arriba" and self.y > 0:
            self.y -= self.velocidad
        elif self.direccion == "abajo" and self.y < pyxel.height - 8:
            self.y += self.velocidad
        elif self.direccion == "izquierda" and self.x > 0:
            self.x -= self.velocidad
        elif self.direccion == "derecha" and self.x < pyxel.width - 8:
            self.x += self.velocidad

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
        pyxel.circ(self.x, self.y, 8, pyxel.COLOR_YELLOW)
        if self.direccion == "derecha":
            pyxel.tri(self.x, self.y, self.x + 8, self.y - 4, self.x + 8, self.y + 4, 0)
        elif self.direccion == "abajo":
            pyxel.tri(self.x, self.y, self.x - 4, self.y + 8, self.x + 4, self.y + 8, 0)
        elif self.direccion == "izquierda":
            pyxel.tri(self.x, self.y, self.x - 8, self.y - 4, self.x - 8, self.y + 4, 0)
        elif self.direccion == "arriba":
            pyxel.tri(self.x, self.y, self.x - 4, self.y - 8, self.x + 4, self.y - 8, 0)


class Fantasma:
    def __init__(self, velocidad: int, direccion, x, y):
        self.velocidad = velocidad
        self.direccion = direccion
        self.x = x
        self.y = y

    def mover(self, pacman):
        # Moverse hacia Pacman de forma simple (puedes mejorar esta lógica)
        if self.x < pacman.x:
            self.x += self.velocidad
        elif self.x > pacman.x:
            self.x -= self.velocidad
        if self.y < pacman.y:
            self.y += self.velocidad
        elif self.y > pacman.y:
            self.y -= self.velocidad

    def draw(self):
        pyxel.rect(self.x, self.y, 8, 8, pyxel.COLOR_RED)


class Consumible:
    def __init__(self, tipo: str, x, y):
        self.tipo = tipo
        self.x = x
        self.y = y

    def activar(self, pacman):
        # Si Pacman está en la misma posición que el consumible
        if pacman.x == self.x and pacman.y == self.y:
            if self.tipo == "fruta":
                pacman.vidas += 1  # Aumentar vidas
            elif self.tipo == "pildora":
                pacman.poder = True  # Activar poder
            elif self.tipo == "puntos":
                # Ganar puntos
                pass
            return True
        return False

    def draw(self):
        if self.tipo == "fruta":
            pyxel.circ(self.x, self.y, 4, pyxel.COLOR_GREEN)
        elif self.tipo == "pildora":
            pyxel.rect(self.x - 2, self.y - 2, 4, 4, pyxel.COLOR_BLUE)
        elif self.tipo == "puntos":
            pyxel.rect(self.x - 1, self.y - 1, 2, 2, pyxel.COLOR_WHITE)


class Pared:
    def __init__(self, posicionX: int, posicionY: int, ancho: int, alto: int):
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.ancho = ancho
        self.alto = alto

    def detectar_colision(self, pacman):
        # Comprobar si Pacman colide con la pared (borde de la pared)
        if (self.posicionX < pacman.x < self.posicionX + self.ancho and 
            self.posicionY < pacman.y < self.posicionY + self.alto):
            return True
        return False

    def draw(self):
        pyxel.rect(self.posicionX, self.posicionY, self.ancho, self.alto, pyxel.COLOR_GRAY)


# Inicialización de Pyxel y creación de instancias
def update():
    pacman.input_direccion()
    pacman.mover()

    for fantasma in fantasmas:
        fantasma.mover(pacman)

    for consumible in consumibles:
        if consumible.activar(pacman):
            consumibles.remove(consumible)

    for pared in paredes:
        if pared.detectar_colision(pacman):
            pacman.vidas -= 1
            pacman.x = 60  # Reposicionar a Pacman
            pacman.y = 60

def draw():
    pacman.draw()
    
    for fantasma in fantasmas:
        fantasma.draw()

    for consumible in consumibles:
        consumible.draw()

    for pared in paredes:
        pared.draw()


# Configuración inicial de Pyxel
pyxel.init(160, 120)

# Crear instancias
pacman = Pacman(2, False, 60, 60)
fantasmas = [Fantasma(1, "arriba", 20, 20), Fantasma(1, "abajo", 120, 80)]
consumibles = [Consumible("fruta", 40, 40), Consumible("pildora", 120, 80), Consumible("puntos", 80, 40)]
paredes = [Pared(30, 30, 50, 10), Pared(90, 40, 10, 50)]

# Ejecutar juego
pyxel.run(update, draw)
