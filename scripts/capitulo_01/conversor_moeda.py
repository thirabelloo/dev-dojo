"""
Conversor de Moedas: Real ↔ Dólar

Este módulo realiza a conversão de valores entre BRL e USD utilizando a cotação atual
obtida via API da AwesomeAPI.
"""

import datetime

import requests


def obter_cotacao_dolar():
    """
    Obtém a cotação atual do dólar em relação ao real via API da AwesomeAPI.

    Returns:
        float: Valor da cotação do dólar (em reais).
        None: Se ocorrer erro na requisição ou na resposta da API.
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


def converter_moeda(valor, cotacao, sentido):
    """
    Converte um valor entre BRL e USD com base na cotação fornecida.

    Args:
        valor (float): Valor a ser convertido.
        cotacao (float): Cotação atual do dólar.
        sentido (str): Direção da conversão. Use "real_para_dolar" ou "dolar_para_real".

    Returns:
        float: Valor convertido com duas casas decimais.

    Raises:
        ValueError: Se a cotação for inválida ou o sentido não reconhecido.
    """

    if cotacao is None or cotacao <= 0:
        raise ValueError("Cotação do dólar inválida ou indisponível.")

    return (
        round(valor / cotacao, 2)
        if sentido == "real_para_dolar"
        else (
            round(valor * cotacao, 2)
            if sentido == "dolar_para_real"
            else ValueError("Sentido de conversão inválido.")
        )
    )


def capturar_valor_usuario(mensagem):
    """
    Solicita ao usuário um valor numérico maior que zero via entrada padrão.

    Args:
        mensagem (str): Texto exibido ao usuário solicitando o valor.

    Returns:
        float: Valor positivo informado pelo usuário.
    """

    while True:
        try:
            valor_solicitado = float(input(mensagem))
            if valor_solicitado > 0:
                return valor_solicitado
            print("O valor precisa ser maior que zero.")
        except ValueError:
            print("Digite apenas números válidos para a conversão.")


def exibir_resultado(valor_origem, valor_convertido, cotacao, origem, destino):
    """
    Exibe na tela o resultado da conversão de moeda com data e cotação utilizada.

    Args:
        valor_origem (float): Valor original informado pelo usuário.
        valor_convertido (float): Valor convertido após cálculo.
        cotacao (float): Cotação do dólar utilizada.
        origem (str): Símbolo da moeda de origem (ex: "R$").
        destino (str): Símbolo da moeda de destino (ex: "US$").
    """

    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    print("\n📊 Resultado da Conversão")
    print(f"Data/Hora: {timestamp}")
    print(f"Cotação do dólar: R$ {cotacao:.2f}")
    print(f"Valor em {origem}: {valor_origem:.2f}")
    print(f"Valor convertido em {destino}: {valor_convertido:.2f}")


def exibir_menu():
    """
    Exibe o menu de opções de conversão e captura a escolha do usuário.

    Returns:
        str: Opção escolhida pelo usuário ("1" ou "2").
    """

    print("💱 Conversor de Moedas")
    print("1 - Real para Dólar")
    print("2 - Dólar para Real")
    return input("Escolha a opção (1 ou 2): ")


def executar_conversao(opcao, cotacao):
    """
    Executa o processo de conversão com base na opção escolhida pelo usuário.

    Args:
        opcao (str): Direção da conversão ("1" para BRL → USD, "2" para USD → BRL).
        cotacao (float): Cotação atual do dólar.

    Raises:
        ValueError: Se a cotação for inválida ou ocorrer erro na conversão.
    """

    if opcao == "1":
        valor = capturar_valor_usuario("Digite o valor em Reais (R$): ")
        convertido = converter_moeda(valor, cotacao, "real_para_dolar")
        exibir_resultado(valor, convertido, cotacao, "R$", "US$")
    elif opcao == "2":
        valor = capturar_valor_usuario("Digite o valor em Dólares (US$): ")
        convertido = converter_moeda(valor, cotacao, "dolar_para_real")
        exibir_resultado(valor, convertido, cotacao, "US$", "R$")
    else:
        print("Opção inválida. Encerrando.")


def main():
    """
    Função principal que coordena o fluxo do programa:
    exibe o menu, obtém a cotação, executa a conversão e exibe o resultado.
    """

    opcao = exibir_menu()
    cotacao = obter_cotacao_dolar()

    if cotacao:
        try:
            executar_conversao(opcao, cotacao)
        except ValueError as e:
            print(f"Erro na conversão: {e}")
    else:
        print("Não foi possível obter a cotação do dólar.")


if __name__ == "__main__":
    main()
