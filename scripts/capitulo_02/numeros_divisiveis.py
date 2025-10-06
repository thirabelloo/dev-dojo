"""
Módulo para coletar números inteiros do usuário e exibir os que são divisíveis por 2 ou 3.
"""


def coletar_numero(posicao):
    """
    Solicita ao usuário um número inteiro na posição indicada.

    Args:
        posicao (int): Índice do número a ser coletado.

    Returns:
        int: Número inteiro informado pelo usuário.
    """

    while True:
        try:
            return int(input(f"Digite o {posicao}º número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


def filtrar_divisiveis_por_2_ou_3(valores):
    """
    Filtra os valores que são divisíveis por 2 ou por 3.

    Args:
        valores (list): Lista de números inteiros.

    Returns:
        set: Conjunto de números divisíveis por 2 ou 3.
    """

    return {valor for valor in valores if valor % 2 == 0 or valor % 3 == 0}


def obter_total_de_entradas():
    """
    Solicita ao usuário o número de valores que serão informados.

    Returns:
        int: Número válido maior que zero.
    """

    while True:
        try:
            total = int(input("Quantos valores você deseja informar? "))
            if total > 0:
                return total
            print("Por favor, insira um número maior que zero.")
        except ValueError:
            print("Valor inválido. Digite apenas números inteiros.")


def main():
    """
    Função principal que coordena a coleta, filtragem e exibição dos números.
    """

    quantidade = obter_total_de_entradas()
    numeros = [coletar_numero(i + 1) for i in range(quantidade)]
    filtrados = filtrar_divisiveis_por_2_ou_3(numeros)
    print(f"Números divisíveis por 2 ou 3: {', '.join(map(str, sorted(filtrados)))}")


if __name__ == "__main__":
    main()
