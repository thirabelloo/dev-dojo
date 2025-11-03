"""
Calculadora Interativa.

Este módulo implementa uma calculadora simples que realiza as operações básicas
de adição, subtração, multiplicação e divisão. O usuário pode interagir com o
programa através de um menu para escolher a operação desejada e fornecer os
números para o cálculo.
"""

# Constantes
SAIR = "0"

TIPO_OPERACOES = {
    "1": "Adição",
    "2": "Subtração",
    "3": "Multiplicação",
    "4": "Divisão",
    SAIR: "Sair",
}


def somar(a, b):
    """
    Realiza a soma de dois números.

    Args:
        a (float): Primeiro número.
        b (float): Segundo número.

    Returns:
        float: Resultado da soma.
    """
    return a + b


def subtrair(a, b):
    """
    Realiza a subtração de dois números.

    Args:
        a (float): Primeiro número.
        b (float): Segundo número.

    Returns:
        float: Resultado da subtração.
    """
    return a - b


def multiplicar(a, b):
    """
    Realiza a multiplicação de dois números.

    Args:
        a (float): Primeiro número.
        b (float): Segundo número.

    Returns:
        float: Resultado da multiplicação.
    """
    return a * b


def dividir(a, b):
    """
    Realiza a divisão de dois números.

    Args:
        a (float): Primeiro número (dividendo).
        b (float): Segundo número (divisor).

    Raises:
        ZeroDivisionError: Se o divisor for zero.

    Returns:
        float: Resultado da divisão.
    """
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b


# Mapeamento de operações para funções
OPERACOES = {
    "1": somar,
    "2": subtrair,
    "3": multiplicar,
    "4": dividir,
}


def coletar_numero(posicao):
    """
    Solicita ao usuário a entrada de um número.

    Args:
        posicao (str): Identificação da posição do número (ex.: "primeiro", "segundo").

    Returns:
        float: Número informado pelo usuário.
    """
    while True:
        try:
            return float(input(f"Informe o {posicao} número: "))
        except ValueError:
            print("Erro: Digite um número válido.")


def exibir_menu():
    """
    Exibe o menu de operações disponíveis e solicita a escolha do usuário.

    Returns:
        str: Operação escolhida pelo usuário.
    """
    print("\nOperações disponíveis:")
    for simbolo, nome in TIPO_OPERACOES.items():
        print(f" {simbolo} -> {nome}")

    while True:
        escolha = input("Escolha a operação desejada: ").strip()
        if escolha in TIPO_OPERACOES:
            return escolha
        print("Operação inválida. Escolha uma operação válida.")


def calcular(operador, a, b):
    """
    Realiza o cálculo com base na operação escolhida e nos números fornecidos.

    Args:
        operador (str): Operação escolhida (ex.: "1" para soma).
        a (float): Primeiro número.
        b (float): Segundo número.

    Returns:
        str: Resultado do cálculo ou mensagem de erro.
    """
    try:
        resultado = OPERACOES[operador](a, b)
        return f"Resultado: {a} {operador} {b} = {resultado}"
    except ZeroDivisionError as e:
        return f"Erro: {e}"


def main():
    """
    Função principal que coordena a execução da calculadora.

    Controla o fluxo do programa, exibindo o menu, coletando os números,
    realizando os cálculos e exibindo os resultados.
    """
    print("🧮 Bem-vindo à Calculadora Interativa!")
    try:
        while True:
            operador = exibir_menu()
            if operador == SAIR:
                print("Encerrando... Obrigado por utilizar a calculadora.")
                break
            x = coletar_numero("primeiro")
            y = coletar_numero("segundo")
            resultado = calcular(operador, x, y)
            print(f"\n{resultado}")
    except KeyboardInterrupt:
        print("\nInterrupção detectada. Encerrando a calculadora com segurança.")


if __name__ == "__main__":
    main()
