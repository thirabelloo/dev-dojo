"""Script que faz a leitura de um valor numérico inteiro e apresentar o valor do número elevado ao quadrado, ao cubo e a 10"""


def operacoes_numero():
    """
    Lê um número inteiro fornecido pelo usuário, calcula o quadrado, o cubo e a décima potência do número, e retorna a soma desses valores.

    Retorna:
    str: Uma string formatada com os resultados das operações e a soma.
    """

    try:
        numero = int(input("Digite o numero:"))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return

    numero_elevado_quadrado = numero**2
    numero_elevado_cubo = numero**3
    numero_elevado_dez = numero**10
    soma = numero_elevado_quadrado + numero_elevado_cubo + numero_elevado_dez

    print(
        f"Número digitado: {numero}\n"
        f"Resultado das operacoes:\n"
        f"Número elevado ao quadrado: {numero_elevado_quadrado}\n"
        f"Número elevado ao cubo: {numero_elevado_cubo}\n"
        f"Número elevado à décima potência: {numero_elevado_dez}\n"
        f"Soma dos resultados: {soma}\n"
    )
