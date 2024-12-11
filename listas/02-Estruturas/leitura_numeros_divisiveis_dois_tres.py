"""Script que faz a leitura de cinco valores numéricos inteiros e apresente somente os que forem divisíveis por 2 ou por 3 """


def obtendo_numeros(numeros):
    """
    Solicita ao usuário que insira um número inteiro e valida se é maior que zero.

    Args:
        numeros (int): A ordem do número a ser inserido.

    Returns:
        int: O número inteiro inserido pelo usuário.
    """
    while True:
        try:
            numero = int(input(f"Digite o valor do {numeros}º numero: "))
            if numero > 0:
                return numero
            return "O número deve ser maior que ZERO."
        except ValueError:
            return "Entrada inválida. Por favor, insira um número."


def filtrando_numeros(numeros):
    """
    Valida e retorna números divisíveis por 2 ou por 3.

    Args:
        numeros (list): A lista de números a serem validados.

    Returns:
        list: Lista de números divisíveis por 2 ou por 3.
    """
    numeros_validos = {
        numero for numero in numeros if numero % 2 == 0 or numero % 3 == 0
    }
    return list(sorted(numeros_validos))


def main():
    """
    Função principal que lê cinco números do usuário, valida-os e imprime os que são divisíveis por 2 ou por 3.
    """
    try:
        total_numeros = 5
        numeros = [obtendo_numeros(i + 1) for i in range(total_numeros)]
        numeros_validos = filtrando_numeros(numeros)
        print("Números divisíveis por 2 ou por 3:", numeros_validos)
    except ValueError as error:
        print(f"Erro: {error}")


main()
