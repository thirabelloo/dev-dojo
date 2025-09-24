"""
Este módulo calcula o valor de uma prestação em atraso, considerando juros e tempo de atraso.
"""


def calcular_prestacao_em_atraso(valor_original, taxa_juros, tempo_atraso):
    """
    Calcula o valor final da prestação em atraso com juros.

    Args:
        valor_original (float): Valor original da prestação.
        taxa_juros (float): Taxa de juros mensal (%).
        tempo_atraso (float): Tempo de atraso em meses.

    Returns:
        float: Valor final da prestação com juros.
    """
    validar_parametro(valor_original, "valor em reais")
    validar_parametro(taxa_juros, "taxa de juros em %")
    validar_parametro(tempo_atraso, "tempo de atraso em dias")
    valor_prestacao = valor_original + (
        valor_original * (taxa_juros / 100) * tempo_atraso
    )
    return round(valor_prestacao, 2)


def validar_parametro(valor_entrada, nome_parametro_parcela):
    """
    Valida se o parâmetro informado é numérico e maior que zero.

    Args:
        valor_entrada (float): Valor a ser validado.
        nome_parametro_parcela (str): Nome do parâmetro para mensagem de erro.

    Raises:
        TypeError: Se o valor não for numérico.
        ValueError: Se o valor for menor ou igual a zero.
    """
    if not isinstance(valor_entrada, (int, float)):
        raise TypeError(f"O valor de '{nome_parametro_parcela}' deve ser numérico.")
    if valor_entrada <= 0:
        raise ValueError(
            f"O valor de '{nome_parametro_parcela}' deve ser maior que zero."
        )


def coletar_dados_usuario(mensagem):
    """
    Solicita ao usuário um valor numérico maior que zero.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        float: Valor informado pelo usuário.
    """
    while True:
        try:
            valor_entrada_usuario = float(input(mensagem))
            if valor_entrada_usuario > 0:
                return valor_entrada_usuario
            print("O valor deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida: Digite um número válido.")


def main():
    """
    Função principal que executa o cálculo da prestação em atraso.
    """
    print("\n📆 Calculadora de Prestação em Atraso")
    valor_original = coletar_dados_usuario(
        "Informe o valor original da prestação (R$): "
    )
    taxa_juros = coletar_dados_usuario("Informe a taxa de juros mensal (%): ")
    tempo_meses = coletar_dados_usuario("Informe o tempo de atraso (meses): ")

    valor_final = calcular_prestacao_em_atraso(valor_original, taxa_juros, tempo_meses)
    print(f"\n💰 Valor da prestação com juros: R$ {valor_final:.2f}\n")


if __name__ == "__main__":
    main()
