"Script que calcule e apresente a área de um círculo."
import math


def calcula_area_circulo(raio):
    """
    Calcula a área de um círculo dado o raio.

    Parâmetros:
        raio (float): O raio do círculo. Deve ser um número positivo.

    Retorna:
        str: A área do círculo formatada com duas casas decimais.
    """
    try:
        if raio < 0:
            raise ValueError("O raio deve ser um numero positivo.")
        area = math.pi * (raio**2)
        print(f"Area do circulo: {area:.2f}")
    except TypeError:
        print("Erro: O valor do raio deve ser um número.")
    except ValueError as error:
        print(f"Erro: {error}. Por favor, forneça um valor positivo para o raio.")
