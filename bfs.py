import time
from collections import deque

class BFS:
    def __init__(self, maze):
        self.maze = maze
        self.start = maze.start
        self.goal = maze.goal

        # Ordre d'exploration cohérent avec DFS
        self.directions = [
            (0, 1),   # droite
            (1, 0),   # bas
            (0, -1),  # gauche
            (-1, 0)   # haut
        ]

    # ---------------------------------------------------------
    # Fonction principale de recherche
    # ---------------------------------------------------------
    def search(self):
        start_time = time.time()

        queue = deque([self.start])   # file FIFO
        visited = set()
        parent = {}

        while queue:
            x, y = queue.popleft()

            if (x, y) in visited:
                continue

            visited.add((x, y))

            # Si on atteint le but
            if (x, y) == self.goal:
                end_time = time.time()
                path = self._reconstruct_path(parent)
                return {
                    "path": path,
                    "explored": visited,
                    "nodes": len(visited),
                    "length": len(path),
                    "time": (end_time - start_time) * 1000  # ms
                }

            # Explorer les voisins
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy

                if (nx, ny) not in visited and self._is_valid(nx, ny):
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))

        # Aucun chemin trouvé (ne devrait jamais arriver)
        return None

    # ---------------------------------------------------------
    # Vérifie si une case est traversable
    # ---------------------------------------------------------
    def _is_valid(self, x, y):
        if 0 <= x < self.maze.size and 0 <= y < self.maze.size:
            return self.maze.grid[x][y] != '#'
        return False

    # ---------------------------------------------------------
    # Reconstruit le chemin depuis le goal jusqu'au start
    # ---------------------------------------------------------
    def _reconstruct_path(self, parent):
        path = []
        node = self.goal

        while node != self.start:
            path.append(node)
            node = parent[node]

        path.append(self.start)
        path.reverse()
        return path
