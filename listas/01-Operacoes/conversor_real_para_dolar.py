"""Script que realiza a conversão de R$ para US$"""

from conversor_dolar_para_real import obtendo_cotacao_dolar


def converter_real_para_dolar():
    """
    Converte um valor em reais para dolares com base na cotação atual.
    Solicita ao usuário que insira um valor em reais e calcula o valor equivalente em dólares.
    """
    cotacao = obtendo_cotacao_dolar()
    if cotacao is None:
        print("Não foi possível obter a cotação do dólar no momento. Tente novamente")
        return

    print(f"A cotação do dólar é: {cotacao:.2f} BRL")

    try:
        usuario_real = float(
            input("Digite o valor em real (R$) para a conversão em dolares(US$): ")
        )
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

    valor_dolar = usuario_real / cotacao
    print(f"A conversão em dolares: {valor_dolar:.2f} US$")
