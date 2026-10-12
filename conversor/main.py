def ler_numero(pergunta):
    """Pede um número ao usuário. Aceita vírgula ou ponto (5,50 ou 5.50)."""
    while True:
        texto = input(pergunta).replace(",", ".")
        try:
            valor = float(texto)
            if valor > 0:
                return valor
            print("Digite um número maior que zero.")
        except ValueError:
            print("Isso não é um número válido, tente de novo.")


print("=== Conversor de Reais para Dólar ===")
cotacao = ler_numero("Quanto vale 1 dólar em reais hoje? (ex: 5,50): ")

while True:
    reais = ler_numero("\nValor em reais: R$ ")
    dolares = reais / cotacao
    print(f"R$ {reais:.2f} = US$ {dolares:.2f}")

    if input("Converter outro valor? (s/n): ").lower() != "s":
        break

print("Até mais!")