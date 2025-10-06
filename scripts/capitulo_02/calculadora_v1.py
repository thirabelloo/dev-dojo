"""
Calculadora interativa que realiza as quatro operações básicas:
adição, subtração, multiplicação e divisão.

O usuário escolhe a operação desejada e informa dois valores numéricos.
O resultado é exibido com validação de entrada e tratamento de erros.
"""

# Mapeamento de operadores para funções matemáticas
OPERACOES = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else float("inf"),
}


def nome_operacao(simbolo):
    """
    Retorna o nome da operação com base no símbolo.

    Args:
        simbolo (str): Símbolo da operação.

    Returns:
        str: Nome da operação.
    """

    return {"+": "Adição", "-": "Subtração", "*": "Multiplicação", "/": "Divisão"}.get(
        simbolo, "Desconhecida"
    )


def exibir_menu():
    """
    Exibe o menu de operações e solicita a escolha do usuário.

    Returns:
        str: Operador escolhido.
    """
    print("\nOperações disponíveis:")
    for simbolo in OPERACOES:
        print(f" {simbolo} -> {nome_operacao(simbolo)}")

    while True:
        operacao = input("Escolha a operação desejada (+, -, *, /): ").strip()
        if operacao in OPERACOES:
            return operacao
        print("Operação inválida. Tente novamente.")


def solicitar_valor(posicao):
    """
    Solicita ao usuário um número decimal, validando a entrada.

    Args:
        posicao (str): Indicação de posição ("primeiro", "segundo").

    Returns:
        float: Valor numérico informado.
    """

    while True:
        try:
            return float(input(f"Digite o {posicao} número: "))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def calculadora(operador, x, y):
    """
    Realiza o cálculo com base na operação escolhida.

    Args:
        operador (str): Operador matemático.
        x (float): Primeiro número.
        y (float): Segundo número.

    Returns:
        str: Resultado formatado ou mensagem de erro.
    """

    resultado = OPERACOES[operador](x, y)
    if resultado == float("inf"):
        return "Erro: divisão por zero não é permitida."
    return f"Resultado: {x} {operador} {y} = {resultado}"


def main():
    """
    Função principal que coordena a execução da calculadora.
    """
    operador = exibir_menu()
    x = solicitar_valor("primeiro")
    y = solicitar_valor("segundo")
    print("\n" + calculadora(operador, x, y))


if __name__ == "__main__":
    main()
