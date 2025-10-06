"""
Módulo que solicita uma quantidade de números inteiros ao usuário,
coleta os valores e exibe o maior e o menor número informado.
"""


def solicitar_quantidade_valores():
    """
    Solicita ao usuário a quantidade de números que deseja informar.
    Garante que o valor seja um inteiro positivo.

    Returns:
        int: Quantidade de números a serem informados.
    """

    while True:
        try:
            quantidade = int(input("Quantos números você deseja informar? "))
            if quantidade > 0:
                return quantidade
            print("Por favor, insira um número maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def solicitar_numero(posicao):
    """
    Solicita ao usuário um número inteiro, indicando sua posição na sequência.

    Args:
        posicao (int): Posição ordinal do número a ser informado.

    Returns:
        int: Número inteiro informado pelo usuário.
    """

    while True:
        try:
            return int(input(f"Digite o {posicao}º número: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def exibir_maior_e_menor(valores):
    """
    Exibe o maior e o menor número de uma lista de inteiros.

    Args:
        valores (list): Lista de números inteiros.
    """

    maior = max(valores)
    menor = min(valores)
    print(f"\nMaior número informado: {maior}")
    print(f"Menor número informado: {menor}")


def main():
    """
    Função principal que coordena a execução do programa.

    Observação:
        O enunciado original do problema solicita exatamente 5 valores.
        No entanto, este programa permite que o usuário escolha quantos valores deseja informar.
    """
    total_numeros = solicitar_quantidade_valores()
    numeros = [solicitar_numero(i + 1) for i in range(total_numeros)]
    exibir_maior_e_menor(numeros)


if __name__ == "__main__":
    main()
