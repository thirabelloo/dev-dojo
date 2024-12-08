"""Script que ler cinco valores numéricos inteiros apresente apenas o maior e o menor deles."""


def obter_numeros_usuario(numero):
    """
    Recebe um número inteiro do usuário.

    Args:
    numero (int): A ordem do número a ser inserido.

    Returns:
    int: O número inteiro validado.
    """
    while True:
        try:
            valor = int(input(f"Digite o {numero}º número: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def maximo_e_minimo_numeros(numeros):
    """
    Retorna o maior e o menor número de uma lista de números.

    Args:
        numeros (list of int): Lista de números inteiros.

    Returns:
        tuple: O maior e o menor número.
    """
    return max(numeros), min(numeros)


def main():
    """
    Função principal que coleta cinco números inteiros do usuário, determina o maior e o menor, e os exibe.
    """
    try:
        total_numeros = 5
        input_obtido = [obter_numeros_usuario(i + 1) for i in range(total_numeros)]
        numero_max, numero_min = maximo_e_minimo_numeros(input_obtido)
        print(f"Maior número: {numero_max}")
        print(f"Menor número: {numero_min}")
    except ValueError as error:
        print(f"Erro: {error}")


main()
