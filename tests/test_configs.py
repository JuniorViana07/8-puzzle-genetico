"""
test_configs.py — Testa o AG com diferentes configurações iniciais.
Compara a performance com o Algoritmo A*.
"""

import sys
import os
import time

# Adiciona a pasta src ao path para importar as classes
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from puzzle import Puzzle
from solver import Solver
from astar import AStarSolver

def run_tests():
    configs = [
        {"nome": "Muito Fácil", "movimentos_embaralhamento": 5},
        {"nome": "Fácil", "movimentos_embaralhamento": 10},
        {"nome": "Médio", "movimentos_embaralhamento": 15},
        {"nome": "Difícil", "movimentos_embaralhamento": 20},
        {"nome": "Muito Difícil", "movimentos_embaralhamento": 25}
    ]

    print(f"{'Configuração':<15} | {'Heurística Inicial':<18} | {'Algoritmo':<10} | {'Solução Encontrada':<20} | {'Tempo (s)':<10} | {'Tamanho do Caminho':<20} | {'Esforço (Gerações/Nós)':<25}")
    print("-" * 135)

    for config in configs:
        # Gera o puzzle na dificuldade
        p = Puzzle()
        p.embaralhar(config["movimentos_embaralhamento"])
        
        custo_inicial = p.custo_manhattan()
        
        # --- TESTE DO ALGORITMO GENÉTICO ---
        ga_solver = Solver(
            puzzle=p,
            tamanho_pop=300,        # População um pouco maior para lidar com o fitness rigoroso
            chance_mutacao=0.20,    
            taxa_crossover=0.85
        )
        
        start_time = time.time()
        # Não passamos callback, então roda silencioso
        melhor = ga_solver.resolver(max_geracoes=3000)
        ga_time = time.time() - start_time
        
        ga_solucao = "Sim" if melhor and melhor.fitness == 0.0 else "Não"
        ga_tamanho = len(melhor.genes) if melhor else "N/A"
        ga_esforco = len(ga_solver.historico_melhor) # número de gerações
        
        print(f"{config['nome']:<15} | {custo_inicial:<18} | {'Genético':<10} | {ga_solucao:<20} | {ga_time:<10.3f} | {ga_tamanho:<20} | {ga_esforco:<25}")
        
        # --- TESTE DO ALGORITMO A* ---
        astar_solver = AStarSolver(p)
        start_time = time.time()
        astar_path = astar_solver.solve()
        astar_time = time.time() - start_time
        
        astar_solucao = "Sim" if astar_path is not None else "Não"
        astar_tamanho = len(astar_path) if astar_path is not None else "N/A"
        astar_esforco = astar_solver.visited_nodes
        
        print(f"{'':<15} | {'':<18} | {'A*':<10} | {astar_solucao:<20} | {astar_time:<10.3f} | {astar_tamanho:<20} | {astar_esforco:<25}")
        print("-" * 135)

if __name__ == "__main__":
    run_tests()
