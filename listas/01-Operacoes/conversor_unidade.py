"""Script que ler uma medida em pés e calcule o equivalente em metros.
"""


def conversor_unidade_ft():
    """
    Converte uma medida em pés (ft) para metros e centímetros.

    Solicita ao usuário que digite uma medida em pés, converte a medida para metros e centímetros, e exibe os resultados.

    Retorna:
        None: Esta função não retorna nenhum valor. Os resultados são impressos diretamente.
    """

    try:
        numero_ft = float(input("Digite o valor da medida em pes(ft):"))
    except ValueError:
        print("Entrada inválida. Por favor, a medida deve ser um numero.")
        return

    ft_para_centimetros = numero_ft * 0.3048
    ft_para_metros = numero_ft * 30.48

    print(
        f"Convertendo {numero_ft} ft:\n"
        f"{ft_para_metros:.2f} metros\n"
        f"{ft_para_centimetros:.2f} centímetros"
    )
