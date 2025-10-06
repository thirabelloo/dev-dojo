"""
Ordenador de Números Inteiros

Este script solicita uma quantidade definida de números inteiros ao usuário
e os exibe em ordem crescente.
"""


def solicitar_numero(posicao):
    """
    Solicita ao usuário um número inteiro.

    Parameters:
        posicao (int): Posição do número (1º, 2º, ...).

    Returns:
        int: Número inteiro informado.
    """
    while True:
        try:
            return int(input(f"Digite o {posicao}º número: "))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def ordenar_numeros(lista_numeros):
    """
    Ordena uma lista de números inteiros em ordem crescente.

    Parameters:
        numeros (list[int]): Lista de números inteiros.

    Returns:
        list[int]: Lista ordenada.
    """
    return sorted(lista_numeros)


def solicitar_quantidade_numeros():
    """
    Solicita ao usuário a quantidade de números a serem informados.

    Returns:
        int: Quantidade válida (maior que zero).
    """
    while True:
        try:
            quantidade = int(
                input("Digite a quantidade de números que deseja ordenar: ")
            )
            if quantidade > 0:
                return quantidade
            print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def main():
    """
    Executa o fluxo principal do programa:
    - Solicita ao usuário a quantidade de números a serem informados
    - Coleta os números individualmente
    - Ordena os valores em ordem crescente
    - Exibe o resultado final
    """

    # Obs.: Embora o problema original sugira o uso fixo de três números, esta versão permite entrada dinâmica.
    quantidade = solicitar_quantidade_numeros()
    lista_numeros = [solicitar_numero(i + 1) for i in range(quantidade)]
    ordenados = ordenar_numeros(lista_numeros)
    print(f"\n📊 Números em ordem crescente: {', '.join(map(str, ordenados))}")


if __name__ == "__main__":
    main()
