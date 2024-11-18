import pyxel

class PacmanGame:
    def __init__(self):
        pyxel.init(160, 120, caption="Pacman")
        self.pacman_x = 80
        self.pacman_y = 60
        self.pacman_dir = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_LEFT):
            self.pacman_x -= 2
            self.pacman_dir = 2
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.pacman_x += 2
            self.pacman_dir = 0
        elif pyxel.btn(pyxel.KEY_UP):
            self.pacman_y -= 2
            self.pacman_dir = 3
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.pacman_y += 2
            self.pacman_dir = 1

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.pacman_x, self.pacman_y, 8, pyxel.COLOR_YELLOW)
        if self.pacman_dir == 0:
            pyxel.tri(self.pacman_x, self.pacman_y, self.pacman_x + 8, self.pacman_y - 4, self.pacman_x + 8, self.pacman_y + 4, 0)
        elif self.pacman_dir == 1:
            pyxel.tri(self.pacman_x, self.pacman_y, self.pacman_x - 4, self.pacman_y + 8, self.pacman_x + 4, self.pacman_y + 8, 0)
        elif self.pacman_dir == 2:
            pyxel.tri(self.pacman_x, self.pacman_y, self.pacman_x - 8, self.pacman_y - 4, self.pacman_x - 8, self.pacman_y + 4, 0)
        elif self.pacman_dir == 3:
            pyxel.tri(self.pacman_x, self.pacman_y, self.pacman_x - 4, self.pacman_y - 8, self.pacman_x + 4, self.pacman_y - 8, 0)

PacmanGame()