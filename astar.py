import time
import heapq

class AStar:
    def __init__(self, maze):
        self.maze = maze
        self.start = maze.start
        self.goal = maze.goal

        # Ordre cohérent : droite, bas, gauche, haut
        self.directions = [
            (0, 1),   # droite
            (1, 0),   # bas
            (0, -1),  # gauche
            (-1, 0)   # haut
        ]

    # ---------------------------------------------------------
    # Heuristique : distance de Manhattan
    # ---------------------------------------------------------
    def heuristic(self, x, y):
        gx, gy = self.goal
        return abs(x - gx) + abs(y - gy)

    # ---------------------------------------------------------
    # Fonction principale de recherche A*
    # ---------------------------------------------------------
    def search(self):
        start_time = time.time()

        # File de priorité : (f(n), g(n), (x, y))
        open_list = []
        heapq.heappush(open_list, (0, 0, self.start))

        visited = set()
        parent = {}
        g_cost = {self.start: 0}

        while open_list:
            f, g, (x, y) = heapq.heappop(open_list)

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

                if not self._is_valid(nx, ny):
                    continue

                new_g = g_cost[(x, y)] + 1

                # Si meilleur chemin trouvé vers ce voisin
                if (nx, ny) not in g_cost or new_g < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_g
                    h = self.heuristic(nx, ny)
                    f = new_g + h
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(open_list, (f, new_g, (nx, ny)))

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
