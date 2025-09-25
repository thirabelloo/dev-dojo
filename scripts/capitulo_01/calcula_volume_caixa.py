"""
Este módulo calcula o valor de uma prestação em atraso, considerando juros e tempo de atraso.
"""


def calcular_volume_caixa(comprimento_com, largura_cm, altura_cm):
    """
    Calcula o valor final da prestação em atraso com juros.

    Args:
        valor_original (float): Valor original da prestação.
        taxa_juros (float): Taxa de juros mensal (%).
        tempo_atraso (float): Tempo de atraso em meses.

    Returns:
        float: Valor final da prestação com juros.
    """
    validar_dimensao(comprimento_com, "comprimento_cm")
    validar_dimensao(largura_cm, "largura da caixa em cm")
    validar_dimensao(altura_cm, "altura da caixa em cm")
    volume_caixa = comprimento_com * largura_cm * altura_cm
    return round(volume_caixa, 2)


def validar_dimensao(valor, nome_parametro):
    """
    Valida se o parâmetro informado é numérico e maior que zero.

    Args:
        valor_entrada (float): Valor a ser validado.
        nome_parametro_parcela (str): Nome do parâmetro para mensagem de erro.

    Raises:
        TypeError: Se o valor não for numérico.
        ValueError: Se o valor for menor ou igual a zero.
    """
    if not isinstance(valor, (int, float)):
        raise TypeError(f"O parâmetro '{nome_parametro}' deve ser numérico.")
    if valor <= 0:
        raise ValueError(f"O parâmetro '{nome_parametro}' deve ser maior que zero.")


def solicitar_dimensao(mensagem):
    """
    Solicita ao usuário um valor numérico maior que zero.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        float: Valor informado pelo usuário.
    """
    while True:
        try:
            dimensao = float(input(mensagem))
            if dimensao > 0:
                return dimensao
            print("Atenção: o valor precisa ser maior que zero. Tente novamente.")
        except ValueError:
            print(
                "Erro: entrada inválida. Digite apenas números, sem letras ou símbolos."
            )


def main():
    """
    Função principal que executa o cálculo da prestação em atraso.
    """
    print("\n📦 Calculadora de Volume de Caixa Retangular")
    comprimento_cm = solicitar_dimensao("Informe o comprimento da caixa (cm): ")
    largura_cm = solicitar_dimensao("Informe a largura da caixa (cm): ")
    altura_cm = solicitar_dimensao("Informe a altura da caixa (cm): ")

    volume_cm3 = calcular_volume_caixa(comprimento_cm, largura_cm, altura_cm)
    print(f"\n📐 Volume da caixa: {volume_cm3:.2f} cm³\n")


if __name__ == "__main__":
    main()
