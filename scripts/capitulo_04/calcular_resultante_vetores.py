"""
Este módulo realiza operações com vetores, incluindo:
- Solicitação de vetores ao usuário.
- Cálculo do produto elemento a elemento entre dois vetores.
- Exibição dos vetores em formato de tabela.

O programa principal solicita dois vetores ao usuário, calcula o vetor resultante
e exibe os três vetores em uma tabela formatada.
"""

from tabulate import tabulate


def exibir_tabela(vetores):
    """
    Exibe os vetores fornecidos em formato de tabela.

    Args:
        vetores (list): Lista de tuplas, onde cada tupla contém um nome (str)
        e uma lista de valores inteiros.

    Returns:
        None
    """

    tabela = [[nome] + valores for nome, valores in vetores]
    print(tabulate(tabela, tablefmt="grid"))


def calcular_multiplicacao(vetor1, vetor2):
    """
    Realiza a multiplicação elemento a elemento entre dois vetores.

    Args:
        vetor1 (list): Lista de inteiros.
        vetor2 (list): Lista de inteiros, do mesmo tamanho que vetor1.

    Returns:
        list: Lista com os produtos correspondentes entre os elementos de vetor1 e vetor2.
    """
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho.")
    return [a * b for a, b in zip(vetor1, vetor2)]


def solicitar_numero_inteiro(mensagem):
    """
    Solicita ao usuário um número inteiro, repetindo até entrada válida.

    Args:
        mensagem (str): Texto a ser exibido ao solicitar o valor.

    Returns:
        int: Número inteiro fornecido pelo usuário.
    """
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def solicitar_tamanho_vetor(texto):
    """
    Solicita ao usuário um número inteiro positivo, repetindo até entrada válida.

    Args:
        texto (str): Texto a ser exibido ao solicitar o valor.

    Returns:
        int: Número inteiro positivo fornecido pelo usuário.
    """
    while True:
        valor = solicitar_numero_inteiro(texto)
        if valor > 0:
            return valor
        print("O número deve ser maior que zero.")


def solicitar_vetor(tamanho, nome):
    """
    Lê uma quantidade fixa de valores inteiros fornecidos pelo usuário para compor um vetor.

    Args:
        tamanho (int): Número de elementos a serem lidos.
        nome (str): Nome do vetor (usado nas mensagens de entrada).

    Returns:
        list: Lista com os inteiros fornecidos pelo usuário.
    """

    return [
        solicitar_numero_inteiro(
            f"Digite um número inteiro para o {nome} [{i + 1}/{tamanho}]: "
        )
        for i in range(tamanho)
    ]


def main():
    """
    Função principal que executa o fluxo completo:
    - Solicita o tamanho dos vetores.
    - Lê os vetores V1 e V2.
    - Calcula o vetor resultado VR.
    - Exibe os três vetores em formato de tabela.

    Returns:
        None
    """

    tamanho = solicitar_tamanho_vetor("Informe o tamanho dos vetores: ")

    print("Preenchendo o vetor V1")
    vetor1 = solicitar_vetor(tamanho, "Vetor 1")

    print("\nPreenchendo o vetor V2:")
    vetor2 = solicitar_vetor(tamanho, "Vetor 2")

    vetor_resultante = calcular_multiplicacao(vetor1, vetor2)
    exibir_tabela([("V1", vetor1), ("V2", vetor2), ("VR", vetor_resultante)])


if __name__ == "__main__":
    main()
