from maze import Maze
from dfs import DFS
from bfs import BFS
from astar import AStar

def print_maze_with_exploration(maze, explored):
    grid = [row[:] for row in maze.grid]

    for (x, y) in explored:
        if grid[x][y] == '.':
            grid[x][y] = 'p'

    for row in grid:
        print("".join(row))
    print()

def print_maze_with_path(maze, path):
    grid = [row[:] for row in maze.grid]

    for (x, y) in path:
        if grid[x][y] not in ('S', 'G'):
            grid[x][y] = '*'

    for row in grid:
        print("".join(row))
    print()

def print_path_list(path):
    s = "Chemin: "
    for (x, y) in path:
        s += f"({x}, {y}) -> "
    print(s[:-4])  # enlever la dernière flèche

def print_stats(name, result):
    print(f"--- {name} ---")
    print(f"Noeuds explorés : {result['nodes']}")
    print(f"Longueur du chemin : {result['length']}")
    print(f"Temps d'exécution : {result['time']:.3f} ms")
    print()

def main():
    # ---------------------------------------------------------
    # Génération du labyrinthe
    # ---------------------------------------------------------
    maze = Maze(size=16, seed=42)
    print("=== Labyrinthe généré ===")
    maze.display()
    print()

    results = {}

    # ---------------------------------------------------------
    # BFS
    # ---------------------------------------------------------
    bfs = BFS(maze)
    res_bfs = bfs.search()
    results["BFS"] = res_bfs

    print("=== Exploration BFS ===")
    print_maze_with_exploration(maze, res_bfs["explored"])

    print("=== Chemin BFS ===")
    print_maze_with_path(maze, res_bfs["path"])

    print_path_list(res_bfs["path"])
    print_stats("BFS", res_bfs)

    # ---------------------------------------------------------
    # DFS
    # ---------------------------------------------------------
    dfs = DFS(maze)
    res_dfs = dfs.search()
    results["DFS"] = res_dfs

    print("=== Exploration DFS ===")
    print_maze_with_exploration(maze, res_dfs["explored"])

    print("=== Chemin DFS ===")
    print_maze_with_path(maze, res_dfs["path"])

    print_path_list(res_dfs["path"])
    print_stats("DFS", res_dfs)

    # ---------------------------------------------------------
    # A*
    # ---------------------------------------------------------
    astar = AStar(maze)
    res_astar = astar.search()
    results["A*"] = res_astar

    print("=== Exploration A* ===")
    print_maze_with_exploration(maze, res_astar["explored"])

    print("=== Chemin A* ===")
    print_maze_with_path(maze, res_astar["path"])

    print_path_list(res_astar["path"])
    print_stats("A*", res_astar)

    # ---------------------------------------------------------
    # Tableau comparatif
    # ---------------------------------------------------------
    print("=== Tableau comparatif ===")
    print(f"{'Algorithme':<12} {'Noeuds':<10} {'Longueur':<10} {'Temps (ms)':<10}")
    for algo, r in results.items():
        print(f"{algo:<12} {r['nodes']:<10} {r['length']:<10} {r['time']:<10.3f}")

if __name__ == "__main__":
    main()
