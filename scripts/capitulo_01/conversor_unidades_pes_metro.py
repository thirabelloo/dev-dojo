"""
Conversor de pés para metros e centímetros.

Este programa solicita ao usuário uma medida em pés (ft), valida a entrada
e exibe o valor equivalente em metros (m) e centímetros (cm).
"""


def coletar_ft(mensagem):
    """
    Solicita ao usuário uma medida em pés com validação.

    Args:
        mensagem (str): Texto exibido ao solicitar o número.

    Returns:
        float: Valor positivo em pés fornecido pelo usuário.
    """

    while True:
        try:
            medida_ft = float(input(mensagem))
            if medida_ft < 0:
                print("A medida deve ser um número positivo. Tente novamente.")
            else:
                return medida_ft
        except ValueError:
            print("Entrada inválida. Digite um valor numérico.")


def converter_ft_para_metros(ft):
    """
    Converte uma medida de pés para metros.

    Args:
        ft (float): Medida em pés.

    Returns:
        float: Medida equivalente em metros.
    """
    return ft * 0.3048


def converter_ft_para_centimetros(ft):
    """
    Converte uma medida de pés para centímetros.

    Args:
        ft (float): Medida em pés.

    Returns:
        float: Medida equivalente em centímetros.
    """
    return ft * 30.48


def exibir_resultado(ft, metros, centimetros):
    """
    Exibe os resultados da conversão com formatação.

    Args:
        ft (float): Medida original em pés.
        metros (float): Medida convertida em metros.
        centimetros (float): Medida convertida em centímetros.
    """
    print(f"\n📐 {ft:.2f} ft equivalem a {metros:.4f} metros.")
    print(f"📐 {ft:.2f} ft equivalem a {centimetros:.2f} centímetros.")


def main():
    """
    Executa a rotina principal do programa.
    """
    print("📏 Conversor de pés para metros e centímetros")
    medida_ft = coletar_ft("Digite a medida em pés (ft): ")
    medida_metros = converter_ft_para_metros(medida_ft)
    medida_centimetros = converter_ft_para_centimetros(medida_ft)
    exibir_resultado(medida_ft, medida_metros, medida_centimetros)


if __name__ == "__main__":
    main()
