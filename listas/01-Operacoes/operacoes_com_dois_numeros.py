"""Script que ler dois valores numéricos inteiros e apresente o resultado das quatro operações aritméticas básicas"""


def operacoes_matematicas():
    """
    Lê dois valores numéricos inteiros fornecidos pelo usuário e realiza quatro operações
    aritméticas básicas: soma, subtração, multiplicação e divisão.
    Em caso de entrada inválida (não numérica), informa o usuário e encerra a função.
    Em caso de tentativa de divisão por zero, informa o usuário e não realiza a operação de divisão.

    Solicita ao usuário:
        - O valor do primeiro número (inteiro)
        - O valor do segundo número (inteiro)

    Calcula e imprime:
        - A soma dos dois números
        - A subtração do segundo número a partir do primeiro
        - A multiplicação dos dois números
        - A divisão do primeiro número pelo segundo, se possível (evitando divisão por zero)
    """

    try:
        numero_one = int(input("Digite o valor do primeiro número: "))
        numero_two = int(input("Digite o valor do segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

    soma = numero_one + numero_two
    subtracao = numero_one - numero_two
    multiplicacao = numero_one * numero_two

    try:
        divisao = numero_one / numero_two
    except ZeroDivisionError:
        divisao = None

    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")

    if divisao is not None:
        print(f"Divisão: {divisao:.2f}")
    else:
        print("Erro: Divisão por zero não é permitida.")
