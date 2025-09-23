"Script que calcule e apresente a área de um círculo."

import math


def calcula_area_circulo(raio):
    """
    Calcula a área de um círculo dado o raio.

    Args:
        raio (float): Raio do círculo. Deve ser um número positivo.

    Returns:
        float: Área do círculo.

    Raises:
        ValueError: Se o raio for negativo.
        TypeError: Se o raio não for numérico.
    """

    if not isinstance(raio, (int, float)):
        raise TypeError("O valor do raio deve ser um número.")

    if raio <= 0:
        raise ValueError("O raio deve ser um numero positivo.")

    return math.pi * (raio**2)


def obter_raio_usuario():
    """
    Solicita ao usuário que insira o valor do raio e o retorna como float.

    Returns:
        float: Valor do raio inserido pelo usuário.
    """
    while True:
        input_user = input("Digite o valor do raio do círculo: ").strip()
        try:
            return float(input_user)
        except ValueError:
            print("Entrada inválida. Digite um número, como 7 ou 3.5.")


def exibir_area_circulo(raio, area):
    """
    Exibe a área do círculo formatada.

    Args:
        raio (float): Raio do círculo.
        area (float): Área do círculo.
    """
    print(f"A área do círculo com raio {raio} cm é: {area:.2f} cm²")


def main():
    """
    Função principal que executa o fluxo do cálculo da área do círculo.
    """
    try:
        raio = obter_raio_usuario()
        area = calcula_area_circulo(raio)
        exibir_area_circulo(raio, area)
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except TypeError as te:
        print(f"Erro de tipo: {te}")


if __name__ == "__main__":
    main()
