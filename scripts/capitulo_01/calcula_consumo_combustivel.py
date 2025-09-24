"""
Este módulo calcula o consumo de combustível para uma viagem,
considerando tempo de viagem, velocidade média e autonomia do veículo.
"""

AUTONOMIA_KM_POR_LITRO = 12


def calcular_consumo_combustivel(tempo_horas, velocidade_kmh):
    """
    Calcula o consumo de combustível em litros para uma viagem.

    Args:
        tempo_horas (float): Tempo da viagem em horas.
        velocidade_kmh (float): Velocidade média em km/h.

    Returns:
        float: Litros de combustível utilizados, com duas casas decimais.

    Raises:
        TypeError: Se os parâmetros não forem numéricos.
        ValueError: Se os parâmetros forem menores ou iguais a zero.
    """

    validar_entrada(tempo_horas, "tempo em horas")
    validar_entrada(velocidade_kmh, "velocidade em km/h")
    distancia_km = tempo_horas * velocidade_kmh
    consumo_por_litro = distancia_km / AUTONOMIA_KM_POR_LITRO
    return round(consumo_por_litro, 2)


def validar_entrada(entrada, nome):
    """
    Valida se o valor é numérico e maior que zero.

    Args:
        valor (float): Valor a ser validado.
        nome (str): Nome do parâmetro para mensagens de erro.

    Raises:
        TypeError: Se o valor não for numérico.
        ValueError: Se o valor for menor ou igual a zero.
    """
    if not isinstance(entrada, (int, float)):
        raise TypeError(f"O valor de '{nome}' deve ser numérico.")
    if entrada <= 0:
        raise ValueError(f"O valor de '{nome}' deve ser maior que zero.")


def solicitar_valor_usuario(mensagem):
    """
    Solicita ao usuário um valor numérico maior que zero.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        float: Valor informado pelo usuário.
    """
    while True:
        try:
            entrada = float(input(mensagem))
            if entrada > 0:
                return entrada
            print("O valor deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def main():
    """
    Função principal que executa o cálculo do consumo de combustível.
    """
    print("\n🚗 Calculadora de Consumo de Combustível")
    tempo = solicitar_valor_usuario("Informe o tempo da viagem (horas): ")
    velocidade = solicitar_valor_usuario("Informe a velocidade média (km/h): ")

    litros_necessarios = calcular_consumo_combustivel(tempo, velocidade)
    print(f"\nLitros de combustível necessários: {litros_necessarios:.2f} L\n")


if __name__ == "__main__":
    main()
