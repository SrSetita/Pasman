import pyxel
import random
class Fantasma:
    def __init__(self, velocidad: int, direccion, x, y, pag, u, v, w, h, colkey):
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
        self.colkey = colkey
        self.velocidad_original = velocidad
        self.u_original = u
        self.v_original = v
        self.punto_inicio = (x, y)  # Guardar el punto de inicio
        self.muerto = False  # El fantasma no está muerto por defecto

    def mover(self, paredes):
        if self.muerto:  # Si está muerto, no se mueve
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

        colision = False
        for pared in paredes:
            if pared.detectar_colision_en_posicion(nueva_x + 8, nueva_y + 8, 8):  # Los fantasmas tienen la colision del sprite
                colision = True
                break

        if colision:
            self.cambiar_direccion()
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
        
        if abs(self.x - pacman.x) < pacman.tamano_colision * 2 and abs(self.y - pacman.y) < pacman.tamano_colision * 2:
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
