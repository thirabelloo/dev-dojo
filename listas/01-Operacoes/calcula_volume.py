"""Script capaz de calcular e apresentar o valor do volume de uma lata de óleo"""

import math


def calcula_volume_lata(raio, altura):
    """
    Calcula o valor do volume de uma lata de oleo.

    Parâmetros:
        raio (float): Raio de circunferencia da lata.
        altura (float): Altura da lata.

    Retorna:
        float: O Volume da lata, formatada com duas casas decimais.
    """
    if not isinstance(raio, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("O raio e altura devem ser um numero")
    volume = math.pi * (raio**2) * altura
    return f"Volume: {volume:.2f} cm³"
