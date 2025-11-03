"""
Calculadora Interativa.

Este módulo implementa uma calculadora simples que realiza operações básicas
como adição, subtração, multiplicação, divisão, potenciação e cálculo de raiz
quadrada inteira. O usuário pode interagir com o programa através de um menu
para escolher a operação desejada e fornecer os números para o cálculo.
"""

import math

# Constantes
SAIR = "0"

# Mapeamento de operações
OPERACOES = {
    "1": {"nome": "Adição", "simbolo": "+", "func": lambda a, b: a + b},
    "2": {"nome": "Subtração", "simbolo": "-", "func": lambda a, b: a - b},
    "3": {"nome": "Multiplicação", "simbolo": "*", "func": lambda a, b: a * b},
    "4": {
        "nome": "Divisão",
        "simbolo": "/",
        "func": lambda a, b: (
            a / b
            if b != 0
            else (_ for _ in ()).throw(
                ZeroDivisionError("Divisão por zero não é permitida.")
            )
        ),
    },
    "5": {"nome": "Potenciação", "simbolo": "**", "func": lambda a, b: a**b},
    "6": {
        "nome": "Raiz quadrada inteira",
        "simbolo": "√",
        "func": lambda a, _: (
            math.isqrt(int(a))
            if a >= 0
            else (_ for _ in ()).throw(
                ValueError("Raiz quadrada de número negativo não é permitida.")
            )
        ),
    },
    SAIR: {"nome": "Sair", "simbolo": "", "func": None},
}


# Entrada de dados
def coletar_numero(mensagem):
    """
    Solicita ao usuário a entrada de um número.

    Args:
        mensagem (str): Mensagem exibida ao usuário para solicitar o número.

    Returns:
        float: Número informado pelo usuário.

    Raises:
        ValueError: Se o valor informado não for um número válido.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido.")


# Exibe o menu de operações
def exibir_menu():
    """
    Exibe o menu de operações disponíveis e solicita a escolha do usuário.

    Returns:
        str: Código da operação escolhida pelo usuário.
    """
    print("\nOperações disponíveis:")
    for codigo, dados in OPERACOES.items():
        print(f" {codigo} -> {dados['nome']}")

    while True:
        escolha = input("Escolha a operação desejada: ").strip()
        if escolha in OPERACOES:
            return escolha
        print("Operação inválida. Escolha uma operação válida.")


# Executa a operação selecionada
def executar_operacao(operador, a, b):
    """
    Executa a operação selecionada com os números fornecidos.

    Args:
        operador (str): Código da operação escolhida.
        a (float): Primeiro número.
        b (float): Segundo número (ignorado para operações unárias como raiz quadrada).

    Returns:
        float: Resultado da operação matemática.

    Raises:
        ValueError: Se o código da operação for inválido.
        ZeroDivisionError: Se houver tentativa de divisão por zero.
        ValueError: Se for solicitado o cálculo da raiz quadrada de um número negativo.
    """

    funcao = OPERACOES[operador]["func"]
    if not funcao:
        raise ValueError("Operação inválida.")
    return funcao(a, b)


# Processa uma operação completa
def processar_operacao(operador):
    """
    Processa a operação matemática com base no código fornecido.

    Para operações binárias (como adição, subtração, multiplicação, etc.), solicita dois números
    ao usuário. Para a operação de raiz quadrada inteira, solicita apenas um número. Em seguida,
    executa o cálculo correspondente e exibe o resultado formatado.

    Args:
        operador (str): Código da operação selecionada pelo usuário.

    Raises:
        ValueError: Se o número informado for inválido ou se for solicitada raiz quadrada de número negativo.
        ZeroDivisionError: Se houver tentativa de divisão por zero.
    """

    simbolo = OPERACOES[operador]["simbolo"]
    if operador == "6":
        valor = coletar_numero(
            "Informe o número para calcular a raiz quadrada inteira: "
        )
        try:
            resultado = executar_operacao(operador, valor, 0)
            print(f"\n📌 Resultado: {simbolo}{int(valor)} = {resultado}")
        except ValueError as e:
            print(f"\nErro: {e}")
    else:
        a = coletar_numero("Informe o 1º número: ")
        b = coletar_numero("Informe o 2º número: ")
        try:
            resultado = executar_operacao(operador, a, b)
            print(f"\n📌 Resultado: {a} {simbolo} {b} = {resultado}")
        except (ZeroDivisionError, ValueError) as e:
            print(f"\nErro: {e}")


# Fluxo principal
def main():
    """Inicia o ciclo principal da calculadora interativa.

    Exibe o menu de operações, processa a escolha do usuário e executa os cálculos
    até que a opção de sair seja selecionada. Também trata interrupções externas como Ctrl+C.
    """

    print("🔢 Calculadora pronta para uso. Vamos começar!")
    try:
        while True:
            operador = exibir_menu()
            if operador == SAIR:
                print("👋 Encerrando... Obrigado por utilizar a calculadora.")
                break
            processar_operacao(operador)
    except KeyboardInterrupt:
        print("\nInterrupção detectada. Finalizando a sessão com segurança.")


if __name__ == "__main__":
    main()
