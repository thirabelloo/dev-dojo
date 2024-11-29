"""Script que realiza a conversão de graus Celsius (C)  para graus Fahrenheit (F). """


def converter_celsius_para_fahrenheit(graus_celsius):
    """
    Converte uma temperatura de Celsius para Fahrenheit.

    Parâmetros:
    graus_celsius (float): A temperatura em graus Celsius.

    Retorna:
    str: A temperatura convertida em Fahrenheit, formatada com duas casas decimais.
    """
    # Verifica se a entrada eh um numero
    if not isinstance(graus_celsius, (int, float)):
        raise TypeError("A temperatura deve ser um numero")
    fahrenheit = (9 / 5 * graus_celsius) + 32
    # Retorna a temperatura formatada
    return f"A temperatura em Fahrenheit eh: {fahrenheit:.2f}"
