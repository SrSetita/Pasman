import pyxel
import math
import random
from pacman import Pacman

def calcular_modulo(x1, y1, x2, y2): #esto se utilizara mas adelante para el movimiento de los fantasmas.
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distancia


class Fantasma:
    def __init__(self, velocidad: int, direccion, x, y, pag, u, v, w, h, t, c, colkey):
        self.muerte_tiempo = 0  # Temporizador para la muerte
        self.velocidad = velocidad
        self.direccion = direccion
        self.x = x
        self.y = y
        self.pag = pag
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.direccion_temp = t #temporizador que marca cuanto tiempo deben mantener la dirección los fantasmas
        self.comportamiento = c #Variable personal de cada fantasma que indica cada cuantos frames cambian de direccion.
        self.colkey = colkey
        self.velocidad_original = velocidad
        self.u_original = u
        self.v_original = v
        self.punto_inicio = (x, y)  # Guardar el punto de inicio
        self.muerto = False  # El fantasma no está muerto por defecto
         #atributo para contar cuantos segundos debe mantener la dirección aleatoria


    def optimo(self, pacman):
        #Esta funcion calcula cual es el mejor movimiento que puede hacer el fantasma
        #se le suman 20 porque es lo que miden nuestras casillas.
        # Cálculo de las distancias con desplazamientos
        result1 = calcular_modulo(self.x + 20, self.y, pacman.x, pacman.y)
        result2 = calcular_modulo(self.x - 20, self.y, pacman.x, pacman.y)
        result3 = calcular_modulo(self.x, self.y + 20, pacman.x, pacman.y)
        result4 = calcular_modulo(self.x, self.y - 20, pacman.x, pacman.y)

        if pacman.poder == True: # Determina el camino más lejos de pacman
            opción = min(result1, result2, result3, result4)
            if opción == result1:
                return "izquierda"
            elif opción == result2:
                return "derecha"
            elif opción == result3:
                return "arriba"
            else: 
                return "abajo"
        else: # Determina el camino más cerca de pacman
            opción = max(result1, result2, result3, result4)
            if opción == result1:
                return "izquierda"
            elif opción == result2:
                return "derecha"
            elif opción == result3:
                return "arriba"
            else: 
                return "abajo"


      
    def mover(self, pacman, paredes):
        if self.muerto:  # Si está muerto, no se mueve
            return
        
        if self.direccion_temp > 0:
            self.direccion_temp -= 1
        else:
            # Calcula la mejor dirección cuando no está bajo el efecto del temporizador
            self.direccion = self.optimo(pacman)

        nueva_x, nueva_y = self.x, self.y
    
        if self.direccion == "arriba":
            nueva_y -= self.velocidad
        elif self.direccion == "abajo":
            nueva_y += self.velocidad
        elif self.direccion == "izquierda":
            nueva_x -= self.velocidad
        elif self.direccion == "derecha":
            nueva_x += self.velocidad

        colision = False
        for pared in paredes:
            if pared.detectar_colision_en_posicion(nueva_x + 8, nueva_y + 8, 8):  # Los fantasmas tienen la colision del sprite
                colision = True
                break

        if colision:
            self.cambiar_direccion()
            self.direccion_temp = self.comportamiento
        else:
            self.x, self.y = nueva_x, nueva_y
        #teletransporte si borde
        if self.x < 0:
            self.x = 440 - 20
        elif self.x > 440:
            self.x = 0 + 20

        if self.y < 0:
            self.y = 390 - 20 - 10
        elif self.y > 390 - 10:
            self.y = 0 + 20


    def cambiar_direccion(self):
        direcciones = ["arriba", "abajo", "izquierda", "derecha"]
        self.direccion = random.choice(direcciones)

    def draw(self):
        if self.muerto:
            return  # No dibujamos el fantasma si está muerto
        #En funcion del frame en el que estemos, dibujará un sprite u otro.
        if (pyxel.frame_count // 12) % 2 == 0: #Contamos los Frames y hacemos division entera.
            pyxel.blt(self.x, self.y, self.pag, self.u, self.v, self.w, self.h, self.colkey)  # Dibuja la primera imagen
        else:
            pyxel.blt(self.x, self.y, self.pag, self.u + 16, self.v, self.w, self.h, self.colkey)   # Dibuja la segunda imagen
        

    def colision_con_pacman(self, pacman):
        # Si el fantasma está en (0, 0), lo ignoramos ya que está "muerto"
        if self.x == 0 and self.y == 0:
            return False
        
        if abs(self.x - pacman.x) < pacman.tamaño_colision * 2 and abs(self.y - pacman.y) < pacman.tamaño_colision * 2:
            return True
        return False

    def morir(self):
        self.muerto = True  # El fantasma está muerto
        self.x, self.y = 0, 0  # Enviamos el fantasma a una posición fuera de la pantalla
        self.muerte_tiempo = 300  # Temporizador de 5 segundos (300 frames a 60 fps)

    def reaparecer(self):
        self.muerto = False  # El fantasma ya no está muerto
        self.x, self.y = self.punto_inicio  # Reiniciar a su posición inicial

    def reset(self):
        self.x, self.y = self.punto_inicio
        self.muerto = False  # Asegurarse de que el fantasma no esté muerto al reiniciar
    def debil(self):
        self.velocidad = 0.5
        self.u = 0
        self.v = 128
