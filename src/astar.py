"""
astar.py — Solver A* para comparação com o Algoritmo Genético.
"""
import heapq
import time
from puzzle import Puzzle, MOVIMENTOS_VALIDOS

class Node:
    def __init__(self, puzzle: Puzzle, parent=None, action=None, g=0):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        self.g = g  # Custo do caminho desde o início (nº de movimentos)
        self.h = puzzle.custo_manhattan()  # Heurística
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f
        
    # Precisamos poder converter o tabuleiro em tupla para usar em um set de visitados
    @property
    def state_tuple(self):
        return tuple(tuple(row) for row in self.puzzle.tabuleiro)


class AStarSolver:
    def __init__(self, puzzle: Puzzle):
        self.initial_puzzle = puzzle
        self.visited_nodes = 0

    def get_solution_path(self, node):
        path = []
        current = node
        while current.parent is not None:
            path.append(current.action)
            current = current.parent
        path.reverse()
        return path

    def solve(self):
        start_node = Node(self.initial_puzzle)
        
        # Fila de prioridade para a fronteira de exploração
        open_set = []
        heapq.heappush(open_set, start_node)
        
        # Conjunto para rastrear estados que já processamos (evita loops)
        closed_set = set()
        closed_set.add(start_node.state_tuple)
        
        self.visited_nodes = 0
        
        while open_set:
            current_node = heapq.heappop(open_set)
            self.visited_nodes += 1
            
            # Checa se é o objetivo
            if current_node.puzzle.esta_resolvido():
                return self.get_solution_path(current_node)
                
            # Gera filhos
            for action in MOVIMENTOS_VALIDOS:
                child_puzzle = current_node.puzzle.copia()
                
                # Se o movimento for válido
                mapa = {
                    "cima": child_puzzle.mover_cima,
                    "baixo": child_puzzle.mover_baixo,
                    "esquerda": child_puzzle.mover_esquerda,
                    "direita": child_puzzle.mover_direita,
                }
                
                if mapa[action]():
                    child_state = child_puzzle.tabuleiro
                    child_tuple = tuple(tuple(row) for row in child_state)
                    
                    if child_tuple not in closed_set:
                        closed_set.add(child_tuple)
                        child_node = Node(child_puzzle, current_node, action, current_node.g + 1)
                        heapq.heappush(open_set, child_node)
                        
        return None  # Nenhuma solução (impossível se gerado por embaralhamento válido)

if __name__ == "__main__":
    p = Puzzle()
    p.embaralhar(20)
    print("Estado inicial:")
    print(p)
    print(f"Manhattan: {p.custo_manhattan()}")
    
    solver = AStarSolver(p)
    start_time = time.time()
    path = solver.solve()
    end_time = time.time()
    
    print("\n=== Solução A* ===")
    print(f"Movimentos ({len(path)}): {path}")
    print(f"Nós expandidos: {solver.visited_nodes}")
    print(f"Tempo: {end_time - start_time:.4f}s")
