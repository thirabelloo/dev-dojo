"""Script que realiza a conversão de US$ para R$"""

import requests


def obtendo_cotacao_dolar():
    """
    Obtém a cotação atual do dólar em relação ao real brasileiro.

    Retorna:
    float: Cotação do dólar em BRL.
    """
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        dolar = float(data["USDBRL"]["bid"])
        return dolar
    except requests.RequestException as error:
        print(f"Erro ao obter a cotação do dólar: {error}")
        return None


def converter_dolar_para_real():
    """
    Converte um valor em dólares para reais com base na cotação atual.
    Solicita ao usuário que insira um valor em dólares e calcula o valor equivalente em reais.
    """
    cotacao = obtendo_cotacao_dolar()
    if cotacao is None:
        print("Não foi possível obter a cotação do dólar no momento.")
        return

    print(f"A cotação do dólar é: {cotacao:.2f} BRL")

    try:
        usuario_real = float(
            input("Digite o valor em dólares (US$) para a conversão em real (R$): ")
        )
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

    valor_real = cotacao * usuario_real
    print(f"A conversão em real: R$ {valor_real:.2f}")
