"""Script que calcula a fatorial de um numero determinado pelo usuario"""


def calcula_fatorial(numero):
    """
    Calcula o fatorial de um número inteiro positivo.

    Parâmetros:
        numero (int): Um número inteiro positivo para calcular o fatorial.
    Retorna:
        str: Uma string indicando o valor do fatorial do número fornecido.

    Levanta:
        ValueError: Se o número for negativo.
    """
    if numero < 0:
        raise ValueError("As entradas devem ser números inteiros positivos.")
    if numero in (0, 1):
        return 1

    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i
    return f"A fatorial de {numero} é {fatorial}"


def operacao_fatorial():
    try:
        numero_usuario = int(
            input("Digite um número inteiro para calcular a fatorial: ")
        )
        resultado = calcula_fatorial(numero_usuario)
        return resultado
    except ValueError:
        return "Erro: Insira um número válido"


print(operacao_fatorial())
