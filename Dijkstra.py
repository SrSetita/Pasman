import pyxel
import heapq

GRID_SIZE = 16  # Size of the grid cells
GRID_WIDTH = 10  # Number of cells horizontally
GRID_HEIGHT = 10  # Number of cells vertically

class Game:
    def __init__(self):
        # Initialize Pyxel
        pyxel.init(GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE, caption="Dijkstra Dot")
        
        # Player start position
        self.player_x = 0
        self.player_y = 0

        # AI start position
        self.ai_x = GRID_WIDTH - 1
        self.ai_y = GRID_HEIGHT - 1

        # Movement cost grid
        self.grid = [[1 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        # Start Pyxel
        pyxel.run(self.update, self.draw)

    def dijkstra(self, start, target):
        """Calculate shortest path from start to target using Dijkstra."""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n, m = GRID_HEIGHT, GRID_WIDTH
        
        distance = [[float('inf')] * m for _ in range(n)]
        distance[start[1]][start[0]] = 0
        pq = [(0, start)]  # (distance, (x, y))
        prev = {start: None}  # To reconstruct the path

        while pq:
            current_dist, (x, y) = heapq.heappop(pq)

            if (x, y) == target:
                break

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_dist = current_dist + self.grid[ny][nx]
                    if new_dist < distance[ny][nx]:
                        distance[ny][nx] = new_dist
                        prev[(nx, ny)] = (x, y)
                        heapq.heappush(pq, (new_dist, (nx, ny)))

        # Reconstruct path
        path = []
        current = target
        while current:
            path.append(current)
            current = prev.get(current)
        path.reverse()
        return path

    def update(self):
        """Update game state."""
        # Player controls
        if pyxel.btnp(pyxel.KEY_UP):
            self.player_y = max(0, self.player_y - 1)
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.player_y = min(GRID_HEIGHT - 1, self.player_y + 1)
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.player_x = max(0, self.player_x - 1)
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.player_x = min(GRID_WIDTH - 1, self.player_x + 1)

        # AI movement
        path = self.dijkstra((self.ai_x, self.ai_y), (self.player_x, self.player_y))
        if len(path) > 1:  # Move to the next step in the path
            self.ai_x, self.ai_y = path[1]

    def draw(self):
        """Draw game state."""
        pyxel.cls(0)  # Clear the screen

        # Draw the grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = 5 if self.grid[y][x] == 1 else 12
                pyxel.rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE, color)

        # Draw the player
        pyxel.circ(self.player_x * GRID_SIZE + GRID_SIZE // 2,
                   self.player_y * GRID_SIZE + GRID_SIZE // 2, 6, pyxel.COLOR_RED)

        # Draw the AI
        pyxel.circ(self.ai_x * GRID_SIZE + GRID_SIZE // 2,
                   self.ai_y * GRID_SIZE + GRID_SIZE // 2, 6, pyxel.COLOR_BLUE)

# Run the game
Game()