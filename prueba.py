import pyxel
import random

# Mapa definido como matriz (0 = vacío, 1 = muro, 2 = punto, 3 = power-up, 4 = fruta)
MAPA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 3, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
    [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1],
    [1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
    [1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1],
    [1, 4, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 3, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1],
    [1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1],
    [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 1, 1],
    [1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1],
    [1, 2, 2, 2, 3, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
]

MAPA2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1],
    [1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1],
    [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 1, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 1, 3, 1],
    [1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
    [1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 1, 2, 2, 1, 2, 2, 3, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 3, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 3, 1, 2, 2, 2, 1],
    [1, 4, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 3, 1, 1, 2, 2, 2, 2, 1, 2, 3, 1, 2, 3, 2, 2, 1, 1, 2, 2, 1],
    [1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1],
    [1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
]

MAPA3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 4, 2, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1],
    [1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 3, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1],
    [1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1],
    [2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 2],
    [2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 2],
    [2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3, 2],
    [1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1],
    [1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
]

GAME_OVER= [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 2, 0, 1, 0, 0, 2, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 0, 2, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 4, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 2, 1, 1, 2, 1, 1, 0, 1, 0, 2, 0, 2, 2, 1, 2, 2, 2, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 0],
    [1, 1, 1, 1, 0, 2, 0, 1, 0, 2, 0, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2, 0],
    [0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 0],
    [0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    
]

game_over = False  # Variable para controlar el estado del juego
inicio = True
puntosmapa = 0
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
            if pared.detectar_colision_en_posicion(nueva_x, nueva_y, self.tamano_colision):
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
        pyxel.circ(self.x, self.y, self.tamano_colision, pyxel.COLOR_YELLOW)
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


import pyxel
import random

import pyxel
import random

class Fantasma:
    def __init__(self, velocidad: int, direccion, x, y, pag, u, v, w, h, colkey):
        self.muerte_tiempo = 0
        self.velocidad = velocidad
        self.direccion = direccion
        self.x = x
        self.y = y
        self.pag = pag
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.colkey = colkey
        self.velocidad_original = velocidad
        self.u_original = u 
        self.v_original = v 
        self.punto_inicio = (x, y)
        self.muerto = False
        self.debil_estado = False

        # Coordenadas de sprites
        self.sprite_coords_vivo = [(u, v), (u + 16, v)]  # Moviéndose
        self.sprite_coords_debil = [(0, 48), (16, 48)]  # Débil

    def mover(self, paredes):
        if self.muerto:
            return

        nueva_x, nueva_y = self.x, self.y

        if self.direccion == "arriba":
            nueva_y -= self.velocidad
        elif self.direccion == "abajo":
            nueva_y += self.velocidad
        elif self.direccion == "izquierda":
            nueva_x -= self.velocidad
        elif self.direccion == "derecha":
            nueva_x += self.velocidad

        if nueva_x < 0 or nueva_x > pyxel.width - self.w or nueva_y < 0 or nueva_y > pyxel.height - self.h:
            self.cambiar_direccion()
            return

        colision = any(
            pared.detectar_colision_en_posicion(nueva_x, nueva_y, self.w)
            for pared in paredes
        )

        if colision:
            self.cambiar_direccion()
        else:
            self.x, self.y = nueva_x, nueva_y

    def cambiar_direccion(self):
        self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    def draw(self):
        """
        Dibuja el fantasma alternando sprites si está vivo,
        usando sprites alternativos si está débil.
        """
        if self.muerto:
            return  # No dibujamos el fantasma si está muerto

        if self.debil_estado:
            # Alternar sprites débil cada 30 frames
            frame_index = (pyxel.frame_count // 30) % len(self.sprite_coords_debil)
            u, v = self.sprite_coords_debil[frame_index]
        else:
            # Alternar sprites vivo cada 30 frames
            frame_index = (pyxel.frame_count // 30) % len(self.sprite_coords_vivo)
            u, v = self.sprite_coords_vivo[frame_index]

        pyxel.blt(self.x, self.y, self.pag, u, v, self.w, self.h, self.colkey)

    def colision_con_pacman(self, pacman):
        if self.x == 0 and self.y == 0:
            return False
        return abs(self.x - pacman.x) < pacman.tamano_colision * 2 and abs(self.y - pacman.y) < pacman.tamano_colision * 2

    def morir(self):
        self.muerto = True
        self.x, self.y = 0, 0  # Enviar a una posición fuera de la pantalla
        self.muerte_tiempo = 300

    def reaparecer(self):
        self.muerto = False
        self.x, self.y = self.punto_inicio

    def reset(self):
        self.x, self.y = self.punto_inicio
        self.muerto = False

    def debil(self):
        self.debil_estado = True
        self.velocidad = 0.5

    def restaurar_estado(self):
        self.debil_estado = False
        self.velocidad = self.velocidad_original



class Consumible:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo

    def activar(self, pacman):
        global puntosmapa
        # Verificar si Pacman está en la misma posición que el consumible
        if abs(self.x - pacman.x) < pacman.tamano_colision * 2 and abs(self.y - pacman.y) < pacman.tamano_colision * 2:
            if self.tipo == 2:  # Punto
                pacman.puntos += 1
                puntosmapa += 1
            elif self.tipo == 3:  # Power-up
                pacman.poder = True
                pacman.poder_tiempo = 600  # Duración del poder (en segundos)
                pacman.velocidad = 3  # Aumentar la velocidad de Pacman
            elif self.tipo == 4:  # Fruta
                pacman.puntos += 5
                pacman.vidas += 1
            return True  # Consumible activado
        return False  # No activado

    def draw(self):
        if self.tipo == 2:  # Punto
            pyxel.rect(self.x - 1, self.y - 1, 3, 3, pyxel.COLOR_WHITE)  # Dibuja el punto
        elif self.tipo == 3:  # Power-up
            pyxel.blt(self.x - 4, self.y - 4, 2, 4, 4, 8, 8, pyxel.COLOR_GRAY)  # Dibuja el power-up
        elif self.tipo == 4:  # Fruta
            pyxel.blt(self.x - 4, self.y - 4, 2, 20, 2, 15, 15, pyxel.COLOR_GRAY)  # Dibuja la fruta


# Función para crear objetos a partir de la matriz
def generar_mapa(pacman):
    paredes = []
    consumibles = []
    global puntosmapa
    if puntosmapa < 192:
        for y, fila in enumerate(MAPA):
            for x, valor in enumerate(fila):
                if valor == 1:
                    paredes.append(Pared(x * 20, y * 20, 20, 20))  # Tamaño de cada celda 20x20
                elif valor in [2, 3, 4]:
                    consumibles.append(Consumible(x * 20 + 10, y * 20 + 10, valor))  # Ajustar posición al centro de la celda
    if puntosmapa >= 192 and puntosmapa < 391:
        for y, fila in enumerate(MAPA2):
            for x, valor in enumerate(fila):
                if valor == 1:
                    paredes.append(Pared(x * 20, y * 20, 20, 20))  # Tamaño de cada celda 20x20
                elif valor in [2, 3, 4]:
                    consumibles.append(Consumible(x * 20 + 10, y * 20 + 10, valor))  # Ajustar posición al centro de la celda
    if puntosmapa >= 391:
        for y, fila in enumerate(MAPA3):
            for x, valor in enumerate(fila):
                if valor == 1:
                    paredes.append(Pared(x * 20, y * 20, 20, 20))  # Tamaño de cada celda 20x20
                elif valor in [2, 3, 4]:
                    consumibles.append(Consumible(x * 20 + 10, y * 20 + 10, valor))  # Ajustar posición al centro de la celda

    return paredes, consumibles

def update():
    global game_over  # Acceder a las variables globales
    global inicio  
    global pacman  
    global paredes  
    global consumibles  
    global fantasmas  
    global puntosmapa
    if puntosmapa == 192 or puntosmapa == 391:
        n = 0
        while n < 1:
            inicio = True
            n += 1
    if game_over:
        return  # Si el juego ha terminado, no actualizamos nada

    pacman.input_direccion()
    pacman.mover(paredes)
    pacman.activar_poder()

    # Verificar si Pac-Man colisiona con algún fantasma
    for fantasma in fantasmas:
        if pacman.poder:
            fantasma.debil()
            
        if pacman.poder and fantasma.colision_con_pacman(pacman):  # Si Pac-Man tiene poder
            fantasma.morir()  # Matar al fantasma
            pacman.puntos += 10  # Ganar puntos por matar al fantasma (opcional)

        elif not pacman.poder and fantasma.colision_con_pacman(pacman):  # Si no tiene poder
            pacman.vidas -= 1
            pacman.x, pacman.y = 210, 90  # Reiniciar posición de Pac-Man
            for fantasma in fantasmas:
                fantasma.reset()  # Reiniciar la posición de los fantasmas

    # Verificar si Pac-Man ha perdido todas las vidas
    if pacman.vidas <= 0:
        game_over = True  # Cambiar el estado del juego a 'terminado'

    # Mover fantasmas
    for fantasma in fantasmas:
        if pacman.poder:
            fantasma.debil()
        else:
            fantasma.velocidad = fantasma.velocidad_original
            fantasma.u = fantasma.u_original
            fantasma.v = fantasma.v_original
        if fantasma.muerto:
            fantasma.muerte_tiempo -= 1  # Reducir el temporizador de muerte
            if fantasma.muerte_tiempo <= 0:
                fantasma.reaparecer()  # Reaparecer el fantasma
        else:
            fantasma.mover(paredes)

    # Verificar si Pac-Man recoge consumibles
    consumibles_restantes = []
    for consumible in consumibles:
        if not consumible.activar(pacman):
            consumibles_restantes.append(consumible)
    consumibles[:] = consumibles_restantes
    if inicio == True:
        pacman = Pacman(2, False, 210, 90)

        # Generar el mapa
        paredes, consumibles = generar_mapa(pacman)

        fantasmas = [Fantasma(0.5, "abajo", 210, 155, 1, 0, 0, 16, 16, pyxel.COLOR_GRAY), Fantasma(1, "arriba", 210, 155, 1, 0, 32, 16, 16, pyxel.COLOR_GRAY), Fantasma(1.5, "abajo", 210, 155, 1, 32, 64, 16, 16, pyxel.COLOR_GRAY), Fantasma(2, "arriba", 210, 155, 1, 0, 96, 16, 16, pyxel.COLOR_GRAY)]


    inicio = False
def draw():
    if game_over:
        pyxel.cls(0)  # Limpiar la pantalla
        pyxel.text(pyxel.width // 2 - 20, pyxel.height // 2, "GAME OVER", pyxel.COLOR_RED)  # Mostrar el mensaje en rojo
        return  # No dibujar más objetos si el juego ha terminado

    pacman.draw()
    for fantasma in fantasmas:
        fantasma.draw()
    for consumible in consumibles:
        consumible.draw()
    for pared in paredes:
        pared.draw()
    pyxel.text(5, 385, f"Puntos: {pacman.puntos} Vidas: {pacman.vidas} Power-up: {int(pacman.poder_tiempo / 60)}", pyxel.COLOR_WHITE)


# Inicialización del juego
pyxel.init(440, 395, title="Pacman Game", fps=60)

#Cargamos los recursos
pyxel.load("my_resource.pyxres")

#Crear a pacman
pacman = Pacman(2, False, 210, 90)

# Generar el mapa
paredes, consumibles = generar_mapa(pacman)

fantasmas = [Fantasma(0.5, "abajo", 210, 155, 1, 0, 0, 16, 16, pyxel.COLOR_GRAY), Fantasma(1, "arriba", 210, 155, 1, 0, 0, 16, 16, pyxel.COLOR_GRAY), Fantasma(1.5, "abajo", 210, 155, 1, 0, 64, 16, 16, pyxel.COLOR_GRAY), Fantasma(2, "arriba", 210, 155, 1, 0, 96, 16, 16, pyxel.COLOR_GRAY)]



pyxel.run(update, draw)