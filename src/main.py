"""
main.py — Ponto de entrada do projeto.

Primeiro: teste no terminal (sem Pygame).
Depois: integre o Pygame para visualização.
"""

import time
from puzzle import Puzzle
from solver import Solver


def main():
    # 1. Criar e embaralhar o puzzle
    puzzle = Puzzle()
    puzzle.embaralhar(100)  # dificuldade média

    print("Estado inicial:")
    print(puzzle)
    print(f"Manhattan: {puzzle.custo_manhattan()}")
    print()

    # 2. Resolver com AG
    solver = Solver(
        puzzle,
        tamanho_pop=200,
        chance_mutacao=0.15,
        taxa_crossover=0.80,
    )

    inicio = time.time()
    melhor = solver.resolver(max_geracoes=2000)
    tempo = time.time() - inicio

    # 3. Exibir resultado
    solver.exibir_resultado()
    print(f"Tempo: {tempo:.2f}s")


if __name__ == "__main__":
    main()
