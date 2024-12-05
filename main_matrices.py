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
    [1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 3, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1],
    [1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1],
    [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 1, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3, 1],
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
    [1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1],
    [2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2],
    [2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2],
    [2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3, 2],
    [1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1],
    [1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
]
import variables_globales as vg



#importar clases
from pacman import Pacman
from pared import Pared
from fantasma import Fantasma
from consumible import Consumible


# Función para crear objetos a partir de la matriz
def generar_mapa(pacman):
    paredes = []
    consumibles = []
    if vg.puntosmapa < 192:
        for y, fila in enumerate(MAPA):
            for x, valor in enumerate(fila):
                if valor == 1:
                    paredes.append(Pared(x * 20, y * 20, 20, 20))  # Tamaño de cada celda 20x20
                elif valor in [2, 3, 4]:
                    consumibles.append(Consumible(x * 20 + 10, y * 20 + 10, valor))  # Ajustar posición al centro de la celda
    if vg.puntosmapa >= 192 and vg.puntosmapa < 386:
        for y, fila in enumerate(MAPA2):
            for x, valor in enumerate(fila):
                if valor == 1:
                    paredes.append(Pared(x * 20, y * 20, 20, 20))  # Tamaño de cada celda 20x20
                elif valor in [2, 3, 4]:
                    consumibles.append(Consumible(x * 20 + 10, y * 20 + 10, valor))  # Ajustar posición al centro de la celda
    if vg.puntosmapa >= 386:
        for y, fila in enumerate(MAPA3):
            for x, valor in enumerate(fila):
                if valor == 1:
                    paredes.append(Pared(x * 20, y * 20, 20, 20))  # Tamaño de cada celda 20x20
                elif valor in [2, 3, 4]:
                    consumibles.append(Consumible(x * 20 + 10, y * 20 + 10, valor))  # Ajustar posición al centro de la celda

    return paredes, consumibles

def update():
    global pacman  
    global paredes  
    global consumibles  
    global fantasmas  
    global victoria
    if vg.puntosmapa == 192 or vg.puntosmapa == 386:
        n = 0
        while n < 1:
            vg.inicio = True
            n += 1
    if vg.puntosmapa == 614:
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
        if pacman.poder: #lineas para movimiento del fantasma
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

    # Verificar si Pac-Man ha perdido todas las vidas
    if vg.vidaspacman <= 0:
        vg.game_over = True  # Cambiar el estado del juego a 'terminado'


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

        fantasmas = [Fantasma(0.5, "izquierda", 200, 140, 1, 0, 0, 16, 16, pyxel.COLOR_GRAY), Fantasma(1, "arriba", 200, 140, 1, 0, 32, 16, 16, pyxel.COLOR_GRAY), Fantasma(1.5, "derecha", 200, 140, 1, 0, 64, 16, 16, pyxel.COLOR_GRAY), Fantasma(2, "arriba", 200, 140, 1, 0, 96, 16, 16, pyxel.COLOR_GRAY)]
    
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

fantasmas = [Fantasma(0.5, "izquierda", 200, 140, 1, 0, 0, 16, 16, pyxel.COLOR_GRAY), Fantasma(1, "arriba", 200, 140, 1, 0, 32, 16, 16, pyxel.COLOR_GRAY), Fantasma(1.5, "derecha", 200, 140, 1, 0, 64, 16, 16, pyxel.COLOR_GRAY), Fantasma(2, "arriba", 200, 140, 1, 0, 96, 16, 16, pyxel.COLOR_GRAY)]



pyxel.run(update, draw)