"""Script que calcula a velocidade em metros por segundo de um projétil"""


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
        raise TypeError(f"{nome} tem que ser um número")


def velocidade_projetil(distancia, tempo):
    """
    Calcula a velocidade em metros por segundo de um projétil que percorre uma distância em quilômetros em um espaço de tempo em minutos.

    Parâmetros:
    distancia (int, float): A distância percorrida em quilômetros. Deve ser um número.
    tempo (int, float): O tempo gasto em minutos. Deve ser um número.

    Retorna:
    str: Uma string formatada com a velocidade em metros por segundo.
    """

    for nomes, valores in [("Distância", distancia), ("Tempo", tempo)]:
        valida_tipo_variavel(nomes, valores)
    if tempo == 0:
        raise ZeroDivisionError("O tempo não pode ser zero")

    velocidade = (distancia * 1000) / (tempo * 60)
    return f"A velocidade do projétil é de {velocidade: .2f} m/s"
