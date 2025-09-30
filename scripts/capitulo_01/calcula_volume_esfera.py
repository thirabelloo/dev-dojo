"""
Calculadora de volume de uma esfera.

Este programa solicita ao usuário o raio da esfera, valida a entrada
e calcula o volume em unidades cúbicas usando a fórmula:
V = (4/3) * π * R³
"""

from math import pi


def coletar_raio(mensagem):
    """
    Solicita ao usuário um valor de raio positivo com validação.

    Args:
        mensagem (str): Texto exibido ao solicitar o número.

    Returns:
        float: Raio positivo fornecido pelo usuário.
    """
    while True:
        try:
            raio = float(input(mensagem))
            if raio <= 0:
                print("O raio deve ser um número positivo. Tente novamente.")
            else:
                return raio
        except ValueError:
            print("Entrada inválida. Digite um valor numérico para o raio.")


def calcular_volume_esfera(raio):
    """
    Calcula o volume de uma esfera com base no raio fornecido.

    Args:
        raio (float): Raio da esfera.

    Returns:
        float: Volume da esfera em unidades cúbicas.
    """
    return (4 / 3) * pi * (raio**3)


def converter_m3_para_cm3(volume_m3):
    """
    Converte volume de metros cúbicos para centímetros cúbicos.

    Args:
        volume_m3 (float): Volume em metros cúbicos.

    Returns:
        float: Volume em centímetros cúbicos.
    """
    return volume_m3 * 1_000_000


def exibir_resultado(volume_m3, volume_cm3):
    """
    Exibe o volume da esfera em m³ e cm³ com formatação.

    Args:
        volume_m3 (float): Volume em metros cúbicos.
        volume_cm3 (float): Volume em centímetros cúbicos.
    """
    print("\n📦 Volume da esfera:")
    print(f"   ➤ {volume_m3:.2f} metros cúbicos (m³)")
    print(f"   ➤ {volume_cm3:.2f} centímetros cúbicos (cm³)")


def main():
    """
    Executa a rotina principal do programa: coleta o raio, calcula e exibe o volume.
    """
    print("⚛️ Calculadora de volume de esfera")
    raio = coletar_raio("Digite o valor do raio: ")
    volume_m3 = calcular_volume_esfera(raio)
    volume_cm3 = converter_m3_para_cm3(volume_m3)
    exibir_resultado(volume_m3, volume_cm3)


if __name__ == "__main__":
    main()
