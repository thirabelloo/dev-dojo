"""Script que realiza a conversão de graus Fahrenheit (F) para graus Celsius (C)."""


def converter_fahrenheit_para_celsius(graus_fahrenheit):
    """
    Converte uma temperatura de Fahrenheit para Celsius.

    Parâmetros:
        graus_fahrenheit (float): A temperatura em graus Fahrenheit.

    Retorna:
        str: A temperatura convertida em Celsius, formatada com duas casas decimais.
    """
    if not isinstance(graus_fahrenheit, (int, float)):
        raise TypeError("A temperatura deve ser um numero")
    celsius = ((graus_fahrenheit - 32) * 5) / 9
    return f"A temperatura em Fahrenheit é: {celsius:.2f}(C)"
