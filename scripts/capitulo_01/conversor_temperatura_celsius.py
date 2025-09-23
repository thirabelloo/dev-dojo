"""
Este módulo realiza a conversão de temperaturas de Fahrenheit para Celsius.
"""


def converter_fahrenheit_para_celsius(graus_fahrenheit):
    """
    Converte uma temperatura de Fahrenheit para Celsius.

    Parâmetros:
        graus_fahrenheit (float): A temperatura em graus Fahrenheit.

    Retorna:
        float: A temperatura convertida em Celsius.

    Raises:
        TypeError: Se o valor fornecido não for numérico.

    """
    if not isinstance(graus_fahrenheit, (int, float)):
        raise TypeError("A temperatura deve ser um numero")
    return ((graus_fahrenheit - 32) * 5) / 9


def main():
    """
    Função principal que solicita uma temperatura em Fahrenheit,
    converte para Celsius e exibe o resultado formatado.
    """
    try:
        temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        temperatura_celsius = converter_fahrenheit_para_celsius(temperatura_fahrenheit)
        print(f"A temperatura em Celsius é: {temperatura_celsius:.2f} °C")
    except ValueError:
        print("Valor inválido. Digite um número válido.")

    except TypeError:
        print("Tipo de entrada incorreto. Certifique-se de que o valor seja numérico.")


if __name__ == "__main__":
    main()
