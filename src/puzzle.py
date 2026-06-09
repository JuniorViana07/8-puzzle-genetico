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
MOVIMENTOS_VALIDOS = ["cima", "baixo", "esquerda", "direita"]

# Movimentos opostos — útil para evitar movimentos que se anulam
OPOSTOS = {"cima": "baixo", "baixo": "cima", "esquerda": "direita", "direita": "esquerda"}

# Estado objetivo: 0 representa o espaço vazio
OBJETIVO = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


class Puzzle:
    """Representa o tabuleiro 3×3 do 8-puzzle."""
    def __init__(self, tabuleiro=None):

        if tabuleiro is None:
            self.tabuleiro = copy.deepcopy(OBJETIVO)
            self.embaralhar(1000)  # embaralha o estado objetivo para criar o estado inicial
            # TODO: inicializar com o ESTADO_OBJETIVO (cópia profunda!)
            pass
        else:
            self.tabuleiro = tabuleiro

    def __str__(self) -> str:
        # TODO: implementar
        linhas = []
        for row in self.tabuleiro:
            linha = "| " + " | ".join(" " if v == 0 else str(v) for v in row) + " |"
            linhas.append(linha)
        return "\n".join(linhas)

    def copia(self) -> "Puzzle":
        novo = Puzzle.__new__(Puzzle)            # cria sem chamar __init__
        novo.tabuleiro = copy.deepcopy(self.tabuleiro)
        return novo

    def encontra_index(self, valor: int) -> tuple[int, int]:
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == valor:
                    return (i, j)
        raise ValueError(f"Valor {valor} não encontrado no tabuleiro.")

    def _trocar(self, a: tuple, b: tuple):
        self.tabuleiro[a[0]][a[1]], self.tabuleiro[b[0]][b[1]] = (
            self.tabuleiro[b[0]][b[1]],
            self.tabuleiro[a[0]][a[1]],
        )

    def mover_esquerda(self) -> bool:
        r, c = self.encontra_index(0)
        if c == 0:
            return False
        self._trocar((r, c), (r, c - 1))
        return True

    def mover_direita(self) -> bool:
        r, c = self.encontra_index(0)
        if c == 2:
            return False
        self._trocar((r, c), (r, c + 1))
        return True

    def mover_cima(self) -> bool:
        r, c = self.encontra_index(0)
        if r == 0:
            return False
        self._trocar((r, c), (r - 1, c))
        return True

    def mover_baixo(self) -> bool:
        r, c = self.encontra_index(0)
        if r == 2:
            return False
        self._trocar((r, c), (r + 1, c))
        return True

    def aplica_movimentos(self, movimentos: list[str]) -> int:
        """Aplica uma lista de movimentos e retorna quantos foram válidos."""
        mapa = {
            "cima": self.mover_cima,
            "baixo": self.mover_baixo,
            "esquerda": self.mover_esquerda,
            "direita": self.mover_direita,
        }
        validos = 0
        # se a solução for encontrada durante o loop, encontramos uma solução de tamanho validos.
        for mov in movimentos:
            if mov in mapa and mapa[mov]():
                validos += 1
        return validos

    def embaralhar(self, iteracoes: int | None = None):
        # TODO: a cada passo, escolher um movimento válido aleatório e aplicar
        # Dica: evite desfazer o movimento anterior (usar OPOSTO)
        if iteracoes is None:
            iteracoes = random.randint(10, 100)
        ultimo_movimento = None
        for _ in range(iteracoes):
            movimento = random.choice(MOVIMENTOS_VALIDOS)
            # Evita desfazer o movimento anterior
            if ultimo_movimento is not None and movimento == OPOSTOS[ultimo_movimento]:
                movimento = random.choice(MOVIMENTOS_VALIDOS)
            
            # Aplicar o movimento
            mapa = {
                "cima": self.mover_cima,
                "baixo": self.mover_baixo,
                "esquerda": self.mover_esquerda,
                "direita": self.mover_direita,
            }
            if movimento in mapa:
                mapa[movimento]()
                ultimo_movimento = movimento

    def custo_manhattan(self) -> float:
        # TODO: para cada valor 1..8, encontrar posição atual e posição
        # no ESTADO_OBJETIVO, somar as distâncias
        """Distância de Manhattan de cada peça até sua posição correta."""
        referencia = {}
        for i in range(3):
            for j in range(3):
                valor = OBJETIVO[i][j]
                referencia[valor] = (i, j)
        distancia = 0.0
        for i in range(3):
            for j in range(3):
                val = self.tabuleiro[i][j]
                if val == 0:
                    continue
                ri, rj = referencia[val]
                distancia += abs(i - ri) + abs(j - rj)
        return distancia

    def esta_resolvido(self) -> bool:
        # TODO: comparar self.tabuleiro com ESTADO_OBJETIVO
        return self.tabuleiro == OBJETIVO
    

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
    print(f"Movimentos válidos: {MOVIMENTOS_VALIDOS}")
