"""
Este módulo calcula o volume de uma lata de óleo com base no raio e altura fornecidos.
"""

from math import pi


def calcular_volume_cilindro(raio_base, altura_cilindro):
    """
    Calcula o volume de uma lata de óleo.

    Args:
        raio_base (float): Raio da lata em centímetros.
        altura_cilindro (float): Altura da lata em centímetros.

    Returns:
        float: Volume da lata arredondado para duas casas decimais.

    Raises:
        TypeError: Se o raio ou altura não forem numéricos.
        ValueError: Se o raio ou altura não forem positivos.
    """
    validar_numero_positivo(raio_base, "raio")
    validar_numero_positivo(altura_cilindro, "altura")
    return round(pi * raio_base**2 * altura_cilindro, 2)


def validar_numero_positivo(valor, nome_parametro):
    """
    Valida se o valor informado é numérico e positivo.

    Args:
        valor (float): Valor a ser validado.
        nome_parametro (str): Nome do parâmetro para mensagem de erro.

    Raises:
        TypeError: Se o valor não for numérico.
        ValueError: Se o valor não for positivo.
    """
    if not isinstance(valor, (int, float)):
        raise TypeError(f"O valor de '{nome_parametro}' deve ser numérico.")
    if valor <= 0:
        raise ValueError(f"O valor de '{nome_parametro}' deve ser positivo.")


def solicitar_valor(mensagem):
    """
    Solicita ao usuário um valor numérico positivo.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        float: Valor informado pelo usuário.
    """
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            print("O valor deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def main():
    """
    Função principal que executa o cálculo do volume da lata de óleo.
    """
    print("\n🛢️ Calculadora de Volume de Lata de Óleo")
    raio = solicitar_valor("Informe o raio da lata (cm): ")
    altura = solicitar_valor("Informe a altura da lata (cm): ")

    volume = calcular_volume_cilindro(raio, altura)
    print(f"\nVolume da lata: {volume:.2f} cm³\n")


if __name__ == "__main__":
    main()
