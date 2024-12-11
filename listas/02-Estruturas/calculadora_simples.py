"""Calculadora simples que realiza as operacoes de: (+, -, * e /)."""


def escolha_operador():
    """
    Solicita ao usuário um operador aritmético e valida a entrada.
    """
    lista_operadores = ["+", "-", "*", "/"]
    while True:
        try:
            operador = input("Digite operador da operacao que deseja realizar: ")
            if operador not in lista_operadores:
                print("Erro: Por favor, insira um operador valido.")
                continue
            return operador
        except ValueError:
            print("Entrada inválida. Por favor, insira uma opcao valida")


def imprime_menu():
    """
    Exibe o menu de operações disponíveis.
    """
    print(
        """
    Calculadora Simples com 2 números\n 
        Operações 
        (+) - Soma 
        (-) - Subtração 
        (*) - Multiplicação 
        (/) - Divisão 
        """
    )


def inserindo_numeros(numero):
    """
    Solicita ao usuário um número e valida a entrada.
    """
    while True:
        try:
            valor = float(input(f"Digite o {numero}º número: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido..")


def operacao_soma(numero_1, numero_2):
    """
    Realiza a soma de dois números.

    Args:
        num1 (float): Primeiro número.
        num2 (float): Segundo número.

    Returns:
        str: Resultado da soma no formato de string.
    """
    return f"\n{numero_1} + {numero_2} = {numero_1 + numero_2}"


def operacao_subtracao(numero_1, numero_2):
    """
    Realiza a subtração de dois números.

    Args:
        num1 (float): Primeiro número.
        num2 (float): Segundo número.

    Returns:
        str: Resultado da subtração no formato de string.
    """
    return f"\n{numero_1} - {numero_2} = {numero_1 - numero_2}"


def operacao_multiplicacao(numero_1, numero_2):
    """
    Realiza a multiplicação de dois números.

    Args:
        num1 (float): Primeiro número.
        num2 (float): Segundo número.

    Returns:
        str: Resultado da multiplicação no formato de string.
    """
    return f"\n{numero_1} * {numero_2} = {numero_1 * numero_2}"


def operacao_divisao(numero_1, numero_2):
    """
    Realiza a divisão de dois números, tratando o caso de divisão por zero.

    Args:
        num1 (float): Primeiro número.
        num2 (float): Segundo número.

    Returns:
        str: Resultado da divisão no formato de string, ou mensagem de erro em caso de divisão por zero.
    """
    try:
        resultado = numero_1 / numero_2
        return f"\n{numero_1} / {numero_2} = {resultado}"
    except ZeroDivisionError:
        return "Erro: Divisão por zero."


def calcular(operador, numero_1, numero_2):
    """
    Realiza a operação aritmética escolhida entre dois números.

    Args:
        operador (str): Operador aritmético escolhido (+, -, *, /).
        numero1 (float): Primeiro número.
        numero2 (float): Segundo número.

    Returns:
        str: Resultado da operação no formato de string.
    """
    operacoes = {
        "+": operacao_soma,
        "-": operacao_subtracao,
        "*": operacao_multiplicacao,
        "/": operacao_divisao,
    }
    return operacoes[operador](numero_1, numero_2)


def calculadora():
    """
    Função principal que executa o fluxo da calculadora.
    Exibe o menu, solicita a operação e os números, executa a operação e exibe o resultado.
    Pergunta ao usuário se deseja realizar outra operação e repete o processo até o usuário optar por sair.
    """
    while True:
        imprime_menu()
        operador = escolha_operador()
        operacao_com_dois_numeros = 2
        numero_1, numero_2 = [
            inserindo_numeros(i + 1) for i in range(operacao_com_dois_numeros)
        ]
        resultado_operacao = calcular(operador, numero_1, numero_2)
        print(resultado_operacao)
        outra_operacao = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if outra_operacao != "s":
            print("Obrigado por usar a calculadora! Até a próxima.")
            break


calculadora()
