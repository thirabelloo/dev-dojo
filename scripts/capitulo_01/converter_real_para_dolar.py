"""
Este módulo converte valores de Real para Dólar utilizando a cotação atual obtida via API.
"""

import datetime

import requests


def obter_cotacao_dolar():
    """
    Obtém a cotação atual do dólar em relação ao real via API.

    Returns:
        float: Cotação do dólar.
        None: Se houver erro na requisição.
    """
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return float(data["USDBRL"]["bid"])
    except requests.RequestException as e:
        print(f"Erro ao obter a cotação do dólar: {e}")
        return None


def converter_real_para_dolar(valor_real, cotacao_dolar):
    """
    Converte um valor em reais para dólares usando a cotação informada.

    Args:
        valor_real (float): Valor em reais.
        cotacao_dolar (float): Cotação do dólar.

    Returns:
        float: Valor convertido em dólares.

    Raises:
        ValueError: Se a cotação for inválida ou indisponível.
    """
    if cotacao_dolar is None or cotacao_dolar <= 0:
        raise ValueError("Cotação do dólar inválida ou indisponível.")
    return round(valor_real / cotacao_dolar, 2)


def exibir_resultado(valor_real, valor_dolar, cotacao):
    """
    Exibe o resultado da conversão de real para dólar.

    Args:
        valor_real (float): Valor em reais.
        valor_dolar (float): Valor convertido em dólares.
        cotacao (float): Cotação utilizada.
    """
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    print("\n📊 Resultado da Conversão")
    print(f"Data/Hora: {timestamp}")
    print(f"Cotação do dólar: R$ {cotacao:.2f}")
    print(f"Valor em Reais: R$ {valor_real:.2f}")
    print(f"Valor em Dólares: US$ {valor_dolar:.2f}")


def capturar_valor_usuario(mensagem):
    """
    Solicita ao usuário um valor numérico maior que zero.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        float: Valor informado pelo usuário.
    """
    while True:
        try:
            valor_solicitado = float(input(mensagem))
            if valor_solicitado > 0:
                return valor_solicitado
            print("O valor precisa ser maior que zero.")
        except ValueError:
            print("Digite apenas números válidos.")


def main():
    """
    Função principal que executa o fluxo de conversão de Real para Dólar.
    """
    print("💵 Conversor de Real para Dólar")
    try:
        valor_real = capturar_valor_usuario("Digite o valor em Reais (R$): ")
        if valor_real <= 0:
            print("O valor deve ser maior que zero.")
            return

        cotacao_dolar = obter_cotacao_dolar()
        valor_dolar = converter_real_para_dolar(valor_real, cotacao_dolar)
        exibir_resultado(valor_real, valor_dolar, cotacao_dolar)
    except ValueError:
        print("Entrada inválida. Digite um número válido.")


if __name__ == "__main__":
    main()
