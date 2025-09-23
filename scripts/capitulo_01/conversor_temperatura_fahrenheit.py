"""
Este módulo realiza a conversão de temperaturas de Celsius para Fahrenheit.
"""


def converter_celsius_para_fahrenheit(graus_celsius):
    """
    Converte uma temperatura de Celsius para Fahrenheit.

    Parâmetros:
    graus_celsius (float): A temperatura em graus Celsius.

    Retorna:
    str: A temperatura convertida em Fahrenheit, formatada com duas casas decimais.
    """
    if not isinstance(graus_celsius, (int, float)):
        raise TypeError("A temperatura deve ser um numero")
    return (9 / 5 * graus_celsius) + 32


def main():
    """
    Função principal que solicita uma temperatura em Celsius,
    converte para Fahrenheit e exibe o resultado formatado.
    """
    try:
        temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
        temperatura_fahrenheit = converter_celsius_para_fahrenheit(temperatura_celsius)
        print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit:.2f} °F")
    except ValueError:
        print(
            "Entrada inválida. Por favor, digite apenas números, sem letras ou símbolos."
        )
    except TypeError:
        print(
            "Tipo de dado incorreto. Certifique-se de inserir um número como 25 ou -3.5."
        )


if __name__ == "__main__":
    main()
