"""
chromosome.py — Representa um indivíduo do Algoritmo Genético.

Cada cromossomo é uma SEQUÊNCIA DE MOVIMENTOS que será aplicada
ao tabuleiro inicial. O fitness mede quão perto do objetivo
essa sequência leva o puzzle.

Implemente DEPOIS de ter puzzle.py funcionando.

Ordem sugerida:
  1. __init__ + calcular_fitness()
  2. crossover()  (método estático)
  3. mutacao()
"""

import random
from puzzle import Puzzle, MOVIMENTOS, OPOSTO


class Chromosome:
    """Um indivíduo: sequência de movimentos + seu fitness."""

    def __init__(self, puzzle, genes=None):
        """
        puzzle: instância de Puzzle (estado inicial, NÃO será modificado)
        genes: lista de movimentos (strings). Se None, gera aleatório.
        """
        self.puzzle = puzzle  # referência ao estado inicial (somente leitura)

        if genes is None:
            # TODO: gerar lista aleatória de movimentos
            # Tamanho entre 15 e 40 (como no repo de referência)
            self.genes = []
        else:
            self.genes = list(genes)  # cópia

        self.fitness = None
        self.dist_manhattan = None
        self.penalidade_tamanho = None

        self.calcular_fitness()

    def get_gene(self):
        vetor = []
    def calcular_fitness(self):
        """
        Aplica os genes ao puzzle (numa CÓPIA) e calcula:
          - dist_manhattan: distância de Manhattan do estado resultante
          - penalidade_tamanho: len(genes) * 0.0001
          - fitness: soma dos dois (ou 0.0 se resolveu)

        Menor fitness = melhor indivíduo.
        """
        # TODO:
        # 1. copia = self.puzzle.copiar()
        # 2. copia.aplicar_sequencia(self.genes)
        # 3. self.dist_manhattan = copia.custo_manhattan()
        # 4. self.penalidade_tamanho = len(self.genes) * 0.0001
        # 5. se copia.esta_resolvido(): fitness = 0.0
        #    senao: fitness = dist_manhattan + penalidade_tamanho
        pass

    @staticmethod
    def crossover(pai_a, pai_b):
        """
        Crossover de ponto único entre dois pais.
        Retorna tupla (filho_a, filho_b).

        Ponto de corte = min(len(a), len(b)) // 2
        Filho A = primeira metade de A + segunda metade de B
        Filho B = primeira metade de B + segunda metade de A
        """
        # TODO: implementar
        pass

    def mutacao(self):
        """
        Aplica UMA mutação ao cromossomo:
          - 50% chance: ADICIONAR um gene ao final
            (evitando desfazer o último movimento)
          - 50% chance: MODIFICAR um gene existente aleatório

        Ao final, recalcular fitness.
        """
        # TODO: implementar
        # Dica: use OPOSTO para verificar se um movimento desfaz o anterior
        pass

    def __repr__(self):
        return f"Chromosome(fitness={self.fitness:.4f}, genes={len(self.genes)})"

    def __str__(self):
        nomes = " → ".join(self.genes[:10])
        if len(self.genes) > 10:
            nomes += f" ... (+{len(self.genes) - 10})"
        return f"({len(self.genes)} movs) {nomes}  [fit={self.fitness:.4f}]"
