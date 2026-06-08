"""
puzzle.py — Representação do tabuleiro 3×3 do 8-puzzle.

COMECE POR AQUI! Este é o alicerce de todo o projeto.
Sem um tabuleiro funcional, nada mais funciona.

Ordem sugerida de implementação:
  1. __init__ e __str__  (visualizar o tabuleiro no terminal)
  2. encontrar_vazio()
  3. movimentos válidos + aplicar_movimento()
  4. copiar()
  5. embaralhar()
  6. custo_manhattan()
  7. esta_resolvido()
"""

import random
import copy


# Movimentos possíveis (direção para onde o ESPAÇO VAZIO se desloca)
MOVIMENTOS = ["cima", "baixo", "esquerda", "direita"]

# Movimentos opostos — útil para evitar movimentos que se anulam
OPOSTO = {
    "cima": "baixo",
    "baixo": "cima",
    "esquerda": "direita",
    "direita": "esquerda",
}

# Estado objetivo: 0 representa o espaço vazio
ESTADO_OBJETIVO = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
]


class Puzzle:
    """Representa o tabuleiro 3×3 do 8-puzzle."""

    def __init__(self, tabuleiro=None):
        """
        Se nenhum tabuleiro for passado, cria o estado resolvido.
        tabuleiro: lista 3×3 (ex: [[0,1,2],[3,4,5],[6,7,8]])
        """
        if tabuleiro is None:
            # TODO: inicializar com o ESTADO_OBJETIVO (cópia profunda!)
            pass
        else:
            self.tabuleiro = tabuleiro

    def __str__(self):
        """
        Retorna uma representação visual do tabuleiro.
        Exemplo:
          | 1 | 2 | 3 |
          | 4 |   | 5 |
          | 6 | 7 | 8 |
        """
        # TODO: implementar
        pass

    def copiar(self):
        """Retorna uma cópia independente deste puzzle."""
        # TODO: usar copy.deepcopy ou copiar manualmente
        pass

    def encontrar_vazio(self):
        """
        Retorna a posição (linha, coluna) do espaço vazio (0).
        Ex: se 0 está no centro, retorna (1, 1).
        """
        # TODO: percorrer self.tabuleiro e encontrar onde está o 0
        pass

    def movimentos_validos(self):
        """
        Retorna lista de movimentos possíveis dado a posição atual do vazio.
        Ex: se vazio está em (0,0), não pode ir para 'cima' nem 'esquerda'.
        """
        # TODO: verificar limites do tabuleiro
        pass

    def aplicar_movimento(self, movimento):
        """
        Aplica um movimento ao tabuleiro (troca o vazio com o vizinho).
        Retorna True se o movimento foi válido, False se foi ignorado.

        Lembre-se: 'cima' significa que o vazio sobe (troca com a peça acima).
        """
        # TODO: implementar a troca
        pass

    def aplicar_sequencia(self, movimentos):
        """
        Aplica uma lista de movimentos em sequência.
        Movimentos inválidos são simplesmente ignorados.
        Retorna o número de movimentos que foram efetivamente aplicados.
        """
        # TODO: iterar e chamar aplicar_movimento para cada um
        pass

    def embaralhar(self, n_movimentos=100):
        """
        Embaralha o tabuleiro a partir do estado resolvido,
        aplicando n_movimentos aleatórios válidos.
        Isso GARANTE que a configuração resultante é resolúvel.
        """
        # TODO: a cada passo, escolher um movimento válido aleatório e aplicar
        # Dica: evite desfazer o movimento anterior (usar OPOSTO)
        pass

    def custo_manhattan(self):
        """
        Calcula a distância de Manhattan total:
        soma de |linha_atual - linha_alvo| + |col_atual - col_alvo|
        para cada peça (exceto o vazio).

        Quanto menor, mais perto da solução. Zero = resolvido.
        """
        # TODO: para cada valor 1..8, encontrar posição atual e posição
        # no ESTADO_OBJETIVO, somar as distâncias
        pass

    def esta_resolvido(self):
        """Retorna True se o tabuleiro está no estado objetivo."""
        # TODO: comparar self.tabuleiro com ESTADO_OBJETIVO
        pass


# ---------------------------------------------------------------------------
# Teste rápido — rode com: python puzzle.py
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    p = Puzzle()
    print("Estado inicial (resolvido):")
    print(p)

    print("\nEmbaralhando...")
    p.embaralhar(20)
    print(p)

    print(f"Manhattan: {p.custo_manhattan()}")
    print(f"Resolvido? {p.esta_resolvido()}")
    print(f"Movimentos válidos: {p.movimentos_validos()}")
