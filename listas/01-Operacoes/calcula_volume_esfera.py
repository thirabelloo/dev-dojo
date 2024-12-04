"""Script que calcula o valor do volume de uma esfera"""

import math


def volume_esfera(raio):
    """
    Calcula o volume de uma esfera dado o seu raio.

    Parâmetros:
    raio (int ou float): O raio da esfera. Deve ser um número positivo.

    Levanta:
    TypeError: Se o raio não for um número (int ou float).
    ValueError: Se o raio for um número negativo.

    Retorna:
    float: O volume da esfera calculado.
    """
    if not isinstance(raio, (int, float)):
        raise TypeError("O raio deve ser um numero.")

    if raio < 0:
        raise ValueError("O raio deve ser um numero positivo")

    volume_metros_cubicos = (4 / 3) * math.pi * (raio**3)
    volume_centimetros_cubicos = volume_metros_cubicos * 1_000_000

    print(
        f"O volume da esfera é {volume_metros_cubicos:.3f} metros cúbicos ou {volume_centimetros_cubicos:.2f} centimetros cúbicos"
    )
