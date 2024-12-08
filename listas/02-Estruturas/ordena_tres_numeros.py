"""Script que dados três números inteiros, apresente-os em ordem crescente"""


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
            nota = float(input(f"Digite o {numero}º número: "))
            return nota
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def ordenazacao_numeros(numeros):
    """
    Ordena uma lista de números inteiros em ordem crescente.

    Args:
        numeros (list of int): Lista de números inteiros.

    Returns:
        list of int: Lista de números inteiros ordenada.
    """
    return sorted(numeros)


def main():
    """
    Função principal que coleta três números inteiros do usuário, os ordena e exibe o resultado.
    """
    try:
        total_numeros = 3
        numeracao = [obter_numeros_usuario(i + 1) for i in range(total_numeros)]
        ordenar_numeros = ordenazacao_numeros(numeracao)
        print(f"Números em ordem crescente: {ordenar_numeros}")

    except ValueError as error:
        print(f"Erro: {error}")
