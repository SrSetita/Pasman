import pyxel
import random
# Mapa definido como matriz (0 = vacío, 1 = muro, 2 = punto, 3 = power-up, 4 = fruta)
MAPA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 3, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
    [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1],
    [1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
    [1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1],
    [1, 4, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 3, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 2, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1],
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
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 3, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1],
    [1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1],
    [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3, 1],
    [1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
    [1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 2, 2, 3, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 3, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 4, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 3, 1, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 3, 2, 2, 1, 1, 2, 2, 1],
    [1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1],
    [1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
]

MAPA3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 4, 2, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1],
    [1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 3, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1],
    [1, 2, 2, 2, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1],
    [2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2],
    [2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2],
    [2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2],
    [1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 3, 1],
    [1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1],
    [1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
]
import variables_globales as vg



#importar clases
from pacman import Pacman
from pared import Pared
from fantasma import Fantasma
from inky import Inky
from blinky import Blinky
from pinky import Pinky
from clyde import Clyde
from consumible import Consumible
from punto import Punto
from fruta import Fruta
from power_up import PowerUp

# Función para crear objetos a partir de la matriz
def generar_mapa(pacman):
    paredes = []
    consumibles = []
    if vg.puntosmapa < 193:
        for y, fila in enumerate(MAPA):
            for x, valor in enumerate(fila):
                if valor == 1:
                    paredes.append(Pared(x * 20, y * 20, 20, 20))  # Tamaño de cada celda 20x20
                elif valor == 2:
                    consumibles.append(Punto(x * 20 + 10, y * 20 + 10))  # Ajustar posición al centro de la celda
                elif valor == 3:
                    consumibles.append(PowerUp(x * 20 + 10, y * 20 + 10))  # Ajustar posición al centro de la celda
                elif valor == 4:
                    consumibles.append(Fruta(x * 20 + 10, y * 20 + 10))  # Ajustar posición al centro de la celda
    if vg.puntosmapa >= 193 and vg.puntosmapa < 390:
        for y, fila in enumerate(MAPA2):
            for x, valor in enumerate(fila):
                if valor == 1:
                    paredes.append(Pared(x * 20, y * 20, 20, 20))  # Tamaño de cada celda 20x20
                elif valor == 2:
                    consumibles.append(Punto(x * 20 + 10, y * 20 + 10))  # Ajustar posición al centro de la celda
                elif valor == 3:
                    consumibles.append(PowerUp(x * 20 + 10, y * 20 + 10))  # Ajustar posición al centro de la celda
                elif valor == 4:
                    consumibles.append(Fruta(x * 20 + 10, y * 20 + 10))  # Ajustar posición al centro de la celda
    if vg.puntosmapa >= 390:
        for y, fila in enumerate(MAPA3):
            for x, valor in enumerate(fila):
                if valor == 1:
                    paredes.append(Pared(x * 20, y * 20, 20, 20))  # Tamaño de cada celda 20x20
                elif valor == 2:
                    consumibles.append(Punto(x * 20 + 10, y * 20 + 10))  # Ajustar posición al centro de la celda
                elif valor == 3:
                    consumibles.append(PowerUp(x * 20 + 10, y * 20 + 10))  # Ajustar posición al centro de la celda
                elif valor == 4:
                    consumibles.append(Fruta(x * 20 + 10, y * 20 + 10))  # Ajustar posición al centro de la celda

    return paredes, consumibles

def update():
    global pacman  
    global paredes  
    global consumibles  
    global fantasmas  
    global victoria
    if vg.puntosmapa == 193 or vg.puntosmapa == 390:
        n = 0
        while n < 1:
            vg.inicio = True
            n += 1
    if vg.puntosmapa == 617:
        vg.victoria = True
    if vg.victoria:
        return
    if vg.game_over:
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
            vg.puntospacman += 10

        elif not pacman.poder and fantasma.colision_con_pacman(pacman):  # Si no tiene poder
            vg.vidaspacman -= 1
            pacman.x, pacman.y = 210, 90  # Reiniciar posición de Pac-Man
            for fantasma in fantasmas:
                fantasma.reset()  # Reiniciar la posición de los fantasmas

    # Verificar si Pac-Man ha perdido todas las vidas
    if vg.vidaspacman <= 0:
        vg.game_over = True  # Cambiar el estado del juego a 'terminado'

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
            fantasma.mover(pacman, paredes)

    # Verificar si Pac-Man recoge consumibles
    consumibles_restantes = []
    for consumible in consumibles:
        if not consumible.activar(pacman):
            consumibles_restantes.append(consumible)
    consumibles[:] = consumibles_restantes
    if vg.inicio == True:
        pacman = Pacman(1.5, False, 210, 90)

        # Generar el mapa
        paredes, consumibles = generar_mapa(pacman)

        fantasmas = [Inky(), Blinky(), Pinky(), Clyde()]

    #verificar si pacman esta lleno
    if vg.vidaspacman >= 5 and not pacman.poder:
        pacman.velocidad = 0.5

    vg.inicio = False
def draw():
    if vg.game_over:
        pyxel.cls(0)  # Limpiar la pantalla
        pyxel.text(pyxel.width // 2 - 20, pyxel.height // 2, "GAME OVER", pyxel.COLOR_RED)
        pyxel.text(pyxel.width // 2 - 20, pyxel.height // 2 + 10, f"Puntos: {vg.puntospacman}", pyxel.COLOR_WHITE)
        return  # No dibujar más objetos si el juego ha terminado
    if vg.victoria:
        pyxel.cls(0)  # Limpiar la pantalla
        pyxel.text(pyxel.width // 2 - 20, pyxel.height // 2, "VICTORIA", pyxel.COLOR_YELLOW)
        pyxel.text(pyxel.width // 2 - 20, pyxel.height // 2 + 10, f"Puntos: {vg.puntospacman}", pyxel.COLOR_WHITE)
        return  # No dibujar más objetos si el juego ha terminado

    pacman.draw()
    for fantasma in fantasmas:
        fantasma.draw()
    for consumible in consumibles:
        consumible.draw()
    for pared in paredes:
        pared.draw()
    pyxel.text(5, 385, f"Puntos: {vg.puntospacman} Vidas: {vg.vidaspacman} Power-up: {int(pacman.poder_tiempo / 60)}", pyxel.COLOR_WHITE)


# Inicialización del juego
pyxel.init(440, 395, title="Pacman Game", fps=60)

#Cargamos los recursos
pyxel.load("my_resource.pyxres")

#Crear a pacman
pacman = Pacman(1.5, False, 210, 90)

# Generar el mapa
paredes, consumibles = generar_mapa(pacman)

fantasmas = [Inky(), Blinky(), Pinky(), Clyde()]



pyxel.run(update, draw)