import random

 
class Maze:
    def __init__(self, size=16):
        self.size = size
        
    # Seed FIXE pour un labyrinthe toujours identique
        random.seed(123)
        
        self.grid = [['#' for _ in range(size)] for _ in range(size)]
        self.start = (1, 1)
        self.goal = (size - 2, size - 2)

        self._generate_empty_border()
        self._generate_path()
        self._add_random_walls()

    # ---------------------------------------------------------
    # 1. Bords extérieurs = murs
    # ---------------------------------------------------------
    def _generate_empty_border(self):
        for i in range(self.size):
            for j in range(self.size):
                if i in (0, self.size - 1) or j in (0, self.size - 1):
                    self.grid[i][j] = '#'
                else:
                    self.grid[i][j] = '.'

    # ---------------------------------------------------------
    # 2. Générer un chemin garanti S → G
    # ---------------------------------------------------------
    def _generate_path(self):
        x, y = self.start
        gx, gy = self.goal

        self.grid[x][y] = 'S'

        # Descendre jusqu'à la ligne du goal
        while x < gx:
            x += 1
            self.grid[x][y] = '.'

        # Aller à droite jusqu'à la colonne du goal
        while y < gy:
            y += 1
            self.grid[x][y] = '.'

        self.grid[gx][gy] = 'G'

    # ---------------------------------------------------------
    # 3. Ajouter des murs aléatoires sans bloquer le chemin
    # ---------------------------------------------------------
    def _add_random_walls(self, wall_probability=0.25):
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                if (i, j) in (self.start, self.goal):
                    continue
                # Ne pas écraser le chemin garanti
                if self.grid[i][j] == '.':
                    if random.random() < wall_probability:
                        self.grid[i][j] = '#'

    # ---------------------------------------------------------
    # Utilitaires
    # ---------------------------------------------------------
    def display(self):
        for row in self.grid:
            print("".join(row))

    def get_neighbors(self, x, y):
        """Retourne les voisins valides (haut, bas, gauche, droite)."""
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        neighbors = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if self.grid[nx][ny] != '#':
                    neighbors.append((nx, ny))
        return neighbors
