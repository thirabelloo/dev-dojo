""" Script que calcula o valor de uma prestação em atraso"""


def valida_tipo_variavel(nome, variavel):
    """
    Valida se uma variável é do tipo int ou float.

    Parâmetros:
        nome (str): O nome da variável para exibir na mensagem de erro.
        variavel (int, float): O valor a ser validado.

    Retorna:
        Nenhum: Lança TypeError se o valor não for int ou float.
    """
    if not isinstance(variavel, (int, float)):
        raise TypeError(f"{nome} deve ser um numero")


def calcula_atraso_prestacao(valor, taxa, tempo):
    """
    Calcula o valor de uma prestação em atraso.

    Parâmetros:
        valor (int, float): O valor original da prestação. Deve ser um número.
        taxa (int, float): A taxa de juros aplicada à prestação. Deve ser um número.
        tempo (int, float): O tempo de atraso em meses. Deve ser um número.

    Retorna:
        float: O valor da prestação em atraso, incluindo juros.
    """
    for nomes, valores in [("Valor", valor), ("Taxa", taxa), ("Tempo", tempo)]:
        valida_tipo_variavel(nomes, valores)

    parcela_atraso = valor + (valor * (taxa / 100) * tempo)
    return f"O valor da prestação em atraso é de R$ {parcela_atraso:.2f}"
