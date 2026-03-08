import time
from collections import deque

class DFS:
    def __init__(self, maze):
        self.maze = maze
        self.start = maze.start
        self.goal = maze.goal

        # Ordre imposé : droite, bas, gauche, haut
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

        stack = deque([self.start])   # pile LIFO optimisée
        visited = set([self.start])   # marquer dès l'empilement
        parent = {}

        while stack:
            x, y = stack.pop()        # plus rapide qu'une liste

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

            # Explorer les voisins dans l'ordre imposé
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy

                if (nx, ny) not in visited and self._is_valid(nx, ny):
                    visited.add((nx, ny))          # marquer ici
                    parent[(nx, ny)] = (x, y)
                    stack.append((nx, ny))

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
