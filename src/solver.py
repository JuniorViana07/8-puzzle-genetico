"""
solver.py — Motor do Algoritmo Genético.

Gerencia a população, aplica seleção, crossover, mutação e elitismo.

Implemente DEPOIS de ter chromosome.py funcionando.

Ordem sugerida:
  1. __init__ + inicializar_populacao()
  2. calcular_fitness_populacao()
  3. selecao_roleta()
  4. aplicar_crossover()
  5. aplicar_mutacao()
  6. elitismo()
  7. resolver() — o loop principal
"""

import random
from chromosome import Chromosome
from puzzle import Puzzle


class Solver:
    """Motor do Algoritmo Genético para o 8-puzzle."""

    def __init__(self, puzzle, tamanho_pop=200, chance_mutacao=0.15,
                 taxa_crossover=0.80):
        """
        puzzle: instância de Puzzle (estado inicial embaralhado)
        """
        self.puzzle = puzzle
        self.tamanho_pop = tamanho_pop
        self.chance_mutacao = chance_mutacao
        self.taxa_crossover = taxa_crossover

        self.populacao = []
        self.melhor = None
        self.fitness_medio = None

        # Histórico para gráficos
        self.historico_melhor = []   # fitness do melhor por geração
        self.historico_medio = []    # fitness médio por geração

    def inicializar_populacao(self):
        """Cria a população inicial com cromossomos aleatórios."""
        # TODO: criar self.tamanho_pop cromossomos usando Chromosome(self.puzzle)
        pass

    def calcular_fitness_populacao(self):
        """
        Atualiza o fitness de todos os cromossomos.
        Atualiza self.melhor e self.fitness_medio.
        """
        # TODO: iterar populacao, recalcular fitness, encontrar o melhor
        pass

    def selecao_roleta(self):
        """
        Seleção por roleta ponderada.
        Retorna 2 cromossomos selecionados.
        Peso = 1 / (0.000001 + fitness)  →  menor fitness = maior peso.
        """
        # TODO: implementar roleta
        pass

    def aplicar_crossover(self):
        """
        Aplica crossover em pares selecionados por roleta.
        Número de cruzamentos = ceil(tamanho_pop * taxa_crossover).
        Filhos são ADICIONADOS à população (será reduzida pelo elitismo).
        """
        # TODO: implementar
        pass

    def aplicar_mutacao(self):
        """Aplica mutação com probabilidade chance_mutacao em cada indivíduo."""
        # TODO: para cada cromossomo, se random() < chance_mutacao: mutacao()
        pass

    def elitismo(self):
        """
        Mantém os 20% melhores, preenche o resto por seleção por roleta.
        Ao final, len(populacao) == tamanho_pop novamente.
        """
        # TODO: ordenar por fitness, manter top 20%, completar com roleta
        pass

    def resolver(self, max_geracoes=2000, callback=None):
        """
        Loop principal do AG.

        callback: função opcional chamada a cada geração com
                  (geracao, melhor, fitness_medio) para atualizar UI.

        Retorna o melhor cromossomo encontrado.
        """
        self.inicializar_populacao()

        for geracao in range(max_geracoes):
            self.aplicar_crossover()
            self.calcular_fitness_populacao()
            self.elitismo()
            self.aplicar_mutacao()

            # Salva histórico
            self.historico_melhor.append(self.melhor.fitness if self.melhor else None)
            self.historico_medio.append(self.fitness_medio)

            # Callback para a UI (Pygame)
            if callback:
                callback(geracao, self.melhor, self.fitness_medio)

            # Critério de parada: solução perfeita
            if self.melhor and self.melhor.fitness == 0.0:
                print(f"✅ Solução encontrada na geração {geracao}!")
                break

            # Log no console
            if geracao % 100 == 0:
                fit = self.melhor.fitness if self.melhor else "?"
                print(f"Geração {geracao}: melhor={fit}, médio={self.fitness_medio:.2f}")

        return self.melhor

    def exibir_resultado(self):
        """Imprime o resultado final no console."""
        if self.melhor is None:
            print("Nenhuma solução encontrada.")
            return

        print("\n" + "=" * 50)
        print("RESULTADO FINAL")
        print("=" * 50)
        print(f"Fitness: {self.melhor.fitness}")
        print(f"Movimentos: {len(self.melhor.genes)}")
        print(f"Sequência: {self.melhor.genes}")

        # Aplicar e mostrar
        copia = self.puzzle.copiar()
        copia.aplicar_sequencia(self.melhor.genes)
        print(f"\nEstado final:")
        print(copia)
        print(f"Resolvido? {copia.esta_resolvido()}")
