
import random

LINHAS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),   # linhas
          (0, 3, 6), (1, 4, 7), (2, 5, 8),   # colunas
          (0, 4, 8), (2, 4, 6)]              # diagonais

notas = {}  # (tabuleiro, jogador, jogada) -> nota


def vencedor(t):
    for a, b, c in LINHAS:
        if t[a] != " " and t[a] == t[b] == t[c]:
            return t[a]
    return None


def jogadas_validas(t):
    return [i for i in range(9) if t[i] == " "]


def escolher(t, jogador, chance_aleatoria):
    validas = jogadas_validas(t)
    if random.random() < chance_aleatoria:
        return random.choice(validas)  # explorar
    estado = "".join(t)
    melhor = max(notas.get((estado, jogador, a), 0) for a in validas)
    empatadas = [a for a in validas if notas.get((estado, jogador, a), 0) == melhor]
    return random.choice(empatadas)


def treinar(partidas=50000):
    for _ in range(partidas):
        t = [" "] * 9
        jogador = "X"
        historico = {"X": [], "O": []}
        while True:
            jogada = escolher(t, jogador, chance_aleatoria=0.3)
            historico[jogador].append(("".join(t), jogador, jogada))
            t[jogada] = jogador
            ganhou = vencedor(t)
            if ganhou or not jogadas_validas(t):
                break
            jogador = "O" if jogador == "X" else "X"

        for j in "XO":
            if ganhou is None:
                recompensa = 0
            elif ganhou == j:
                recompensa = 1
            else:
                recompensa = -1
            for chave in historico[j]:
                antiga = notas.get(chave, 0)
                notas[chave] = antiga + 0.1 * (recompensa - antiga)


def mostrar(t):
    def c(i):
        return t[i] if t[i] != " " else str(i + 1)
    print(f"\n {c(0)} | {c(1)} | {c(2)}")
    print("---+---+---")
    print(f" {c(3)} | {c(4)} | {c(5)}")
    print("---+---+---")
    print(f" {c(6)} | {c(7)} | {c(8)}\n")


def jogar():
    t = [" "] * 9
    humano, ia = "X", "O"
    vez = "X"
    while True:
        mostrar(t)
        if vez == humano:
            while True:
                texto = input("Sua jogada (1-9): ")
                if texto.isdigit() and 1 <= int(texto) <= 9 and t[int(texto) - 1] == " ":
                    jogada = int(texto) - 1
                    break
                print("Jogada inválida, tente de novo.")
        else:
            jogada = escolher(t, ia, chance_aleatoria=0)
            print(f"A IA jogou na casa {jogada + 1}.")
        t[jogada] = vez

        ganhou = vencedor(t)
        if ganhou or not jogadas_validas(t):
            mostrar(t)
            if ganhou == humano:
                print("Você ganhou!")
            elif ganhou == ia:
                print("A IA ganhou!")
            else:
                print("Empate!")
            return
        vez = ia if vez == humano else humano


if __name__ == "__main__":
    print("A IA está treinando (jogando 100 mil partidas contra si mesma)...")
    treinar()
    print("Pronto! Você é o X e começa. As casas são numeradas de 1 a 9.")
    while True:
        jogar()
        if input("Jogar de novo? (s/n): ").lower() != "s":
            break