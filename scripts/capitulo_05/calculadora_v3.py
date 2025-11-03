"""
Calculadora Interativa.

Este módulo implementa uma calculadora simples que realiza as operações básicas
de adição, subtração, multiplicação e divisão. O usuário pode interagir com o
programa através de um menu para escolher a operação desejada e fornecer os
números para o cálculo.
"""

# Constantes
EXIT = "0"


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
    "1": {"nome": "Adição", "simbolo": "+", "func": somar},
    "2": {"nome": "Subtração", "simbolo": "-", "func": subtrair},
    "3": {"nome": "Multiplicação", "simbolo": "*", "func": multiplicar},
    "4": {"nome": "Divisão", "simbolo": "/", "func": dividir},
    EXIT: {"nome": "Sair", "simbolo": "", "func": None},
}


def solicitar_numero(mensagem):
    """
    Solicita ao usuário a entrada de um número decimal válido.

    Args:
        mensagem (str): Texto exibido ao usuário.

    Returns:
        float: Número digitado pelo usuário.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")


def exibir_menu_operacoes():
    """
    Exibe o menu de operações disponíveis e solicita a escolha do usuário.

    Returns:
        str: Código da operação escolhida.
    """

    print("\nMenu de Operações Disponíveis:")
    for codigo, dados_operacao in OPERACOES.items():
        print(f" {codigo} -> {dados_operacao['nome']}")

    while True:
        escolha_operacao = input("Escolha a operação desejada: ").strip()
        if escolha_operacao in OPERACOES:
            return escolha_operacao
        print("Operação inválida. Escolha uma operação válida.")


def aplicar_operacao(codigo_operacao, numero1, numero2):
    """
    Executa a operação matemática com os números fornecidos.

    Args:
        codigo_operacao (str): Código da operação.
        numero1 (float): Primeiro número.
        numero2 (float): Segundo número.

    Returns:
        float: Resultado da operação.

    Raises:
        ValueError: Se o código da operação for inválido.
    """
    operacao = OPERACOES[codigo_operacao]["func"]
    if not operacao:
        raise ValueError("Operação inválida.")
    return operacao(numero1, numero2)


def processar_operacao(operador):
    """
    Processa a operação escolhida pelo usuário e exibe o resultado formatado.

    Args:
        codigo_operacao (str): Código da operação selecionada.
    """
    simbolo = OPERACOES[operador]["simbolo"]
    numero1 = solicitar_numero("Informe o 1º número: ")
    numero2 = solicitar_numero("Informe o 2º número: ")
    try:
        resultado = aplicar_operacao(operador, numero1, numero2)
        print(f"\n📌 Resultado: {numero1} {simbolo} {numero2} = {resultado}")
    except (ZeroDivisionError, ValueError) as e:
        print(f"\nErro: {e}")


def main():
    """
    Função principal que coordena a execução da calculadora.

    Controla o fluxo do programa, exibindo o menu, coletando os números,
    realizando os cálculos e exibindo os resultados.
    """
    print("🧮 Bem-vindo à Calculadora Interativa!")
    try:
        while True:
            codigo_operacao = exibir_menu_operacoes()
            if codigo_operacao == EXIT:
                print("Encerrando... Obrigado por utilizar a calculadora.")
                break
            processar_operacao(codigo_operacao)
    except KeyboardInterrupt:
        print("\nInterrupção detectada. Encerrando a calculadora com segurança.")


if __name__ == "__main__":
    main()
