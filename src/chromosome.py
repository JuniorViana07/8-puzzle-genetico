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

from puzzle import Puzzle, MOVIMENTOS_VALIDOS, OPOSTOS


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
            self.genes = self.get_gene()
        else:
            self.genes = list(genes)  # cópia

        self.fitness = float("inf")
        self.dist_manhattan = float("inf")
        self.penalidade_tamanho = 0.0

        self.calcula_fitness()

    def get_gene(self):
        vetor = []
        tam_genoma = random.choice(range(15, 40))
        ultimo = None
        for _ in range(tam_genoma):
            novo = random.choice(MOVIMENTOS_VALIDOS)
            if(ultimo is not None):
                while novo == OPOSTOS[ultimo]:
                    novo = random.choice(MOVIMENTOS_VALIDOS)
            vetor.append(novo)
            ultimo = novo
        return vetor

    def calcula_fitness(self):
        temp = self.puzzle.copia()

        for indice, mov in enumerate(self.genes):
            mapa = {
            "cima": temp.mover_cima,
            "baixo": temp.mover_baixo,
            "esquerda": temp.mover_esquerda,
            "direita": temp.mover_direita,
            }
            if mov in mapa:
                mapa[mov]()
                
            if temp.esta_resolvido():
                self.genes = self.genes[: indice + 1]
                self.fitness = 0.0
                self.distancia_custo = 0.0
                self.erro_tamanho = 0.0
                return

        self.distancia_custo = temp.custo_manhattan()
        self.erro_tamanho = len(self.genes) * 0.001  # Aumentado de 0.0001 para ter mais peso
        self.fitness = self.distancia_custo + self.erro_tamanho

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
        # Garante que `a` é o melhor pai
        if pai_b.fitness < pai_a.fitness:
            pai_a, pai_b = pai_b, pai_a
 
        ponto = min(len(pai_a.genes), len(pai_b.genes)) // 2
 
        genes_a = pai_a.genes[:ponto] + pai_b.genes[ponto:]
        genes_b = pai_b.genes[:ponto] + pai_a.genes[ponto:]
 
        return (
            Chromosome(pai_a.puzzle, genes_a),
            Chromosome(pai_b.puzzle, genes_b),
        )

    def mutacao(self, so_crescer : bool = False):
        """
        Aplica UMA mutação ao cromossomo:
          - 50% chance: ADICIONAR um gene ao final
            (evitando desfazer o último movimento)
          - 50% chance: MODIFICAR um gene existente aleatório

        Ao final, recalcular fitness.
        """
        if self.distancia_custo > 2:
            so_crescer = True
        # TODO: implementar
        # Dica: use OPOSTO para verificar se um movimento desfaz o anterior
        if not self.genes:
            # Cromossomo vazio: força adição
            self.genes.append(random.choice(MOVIMENTOS_VALIDOS))
            self.calcula_fitness()
            return
 
        chance_adicionar = 0.5 if not so_crescer else 1.0
 
        if random.random() < chance_adicionar:
            # Adiciona um movimento no final evitando desfazer o último
            ultimo = self.genes[-1]
            novo = random.choice(MOVIMENTOS_VALIDOS)
            while novo == OPOSTOS[ultimo]:
                novo = random.choice(MOVIMENTOS_VALIDOS)
            self.genes.append(novo)
        else:
            # Modifica um gene existente aleatório
            idx = random.randint(0, len(self.genes) - 1)
            original = self.genes[idx]
            novo = random.choice(MOVIMENTOS_VALIDOS)
            while novo == original:
                novo = random.choice(MOVIMENTOS_VALIDOS)
            self.genes[idx] = novo
 
        self.calcula_fitness()

    def __repr__(self):
        return f"Chromosome(fitness={self.fitness:.4f}, genes={len(self.genes)})"

    def __str__(self):
        nomes = " → ".join(self.genes[:10])
        if len(self.genes) > 10:
            nomes += f" ... (+{len(self.genes) - 10})"
        return f"({len(self.genes)} movs) {nomes}  [fit={self.fitness:.4f}]"
