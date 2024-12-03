import pyxel

def alternar_imagenes():
    pyxel.init(160, 120, title="Alternar Imágenes")  # Inicia una ventana de 160x120
    pyxel.load("my_resource.pyxres")  # Carga el archivo con las imágenes

    def update():
        # No necesitamos lógica adicional en este ejemplo para update.
        pass

    def draw():
        pyxel.cls(0)  # Limpia la pantalla con color negro (0)
        # Alterna entre imágenes cada 30 frames
        if (pyxel.frame_count // 5) % 2 == 0:
            pyxel.blt(60, 40, 1, 0, 16, 16, 16, 0)  # Dibuja la primera imagen
        else:
            pyxel.blt(60, 40, 1, 16, 16, 16, 16, 0)   # Dibuja la segunda imagen

    pyxel.run(update, draw)  # Ejecuta el bucle principal

if __name__ == "__main__":
    alternar_imagenes()