import pyxel

class PacmanGame:
    def __init__(self):
        pyxel.init(160, 120, caption="Pacman")
        self.pacman_x = 80
        self.pacman_y = 60
        self.pacman_dir = 0
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_LEFT):
            self.pacman_x -= 2
            self.pacman_dir = 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.pacman_x += 2
            self.pacman_dir = 0
        if pyxel.btn(pyxel.KEY_UP):
            self.pacman_y -= 2
            self.pacman_dir = 3
        if pyxel.btn(pyxel.KEY_DOWN):
            self.pacman_y += 2
            self.pacman_dir = 1

PacmanGame()