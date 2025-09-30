"""
Calculadora de velocidade de projétil.

Este script permite calcular a velocidade média de um projétil em metros por segundo (m/s),
com base na distância percorrida em quilômetros e no tempo gasto em minutos.
"""


def coletar_valor(texto):
    """
    Solicita ao usuário um valor numérico decimal com validação.

    Parâmetros:
        texto (str): Mensagem exibida ao solicitar o valor.

    Retorna:
        float: Valor numérico fornecido pelo usuário.
    """

    while True:
        try:
            return float(input(texto))
        except ValueError:
            print(
                "Entrada incorreta. Para calcular a velocidade, insira um valor numérico válido."
            )


def calcular_velocidade(distancia_km, tempo):
    """
    Calcula a velocidade média de um projétil em m/s.

    Parâmetros:
        distancia_km (float): Distância percorrida em quilômetros.
        tempo (float): Tempo gasto em minutos.

    Retorna:
        float ou None: Velocidade em metros por segundo, ou None se o tempo for zero.
    """

    if tempo == 0:
        return None
    return (distancia_km * 1000) / (tempo * 60)


def main():
    """
    Função principal que executa a coleta de dados, cálculo e exibição da velocidade.
    """

    print("🚀 Calculadora de velocidade de projétil")
    distancia = coletar_valor("Digite a distância em quilômetros: ")
    tempo = coletar_valor("Digite o tempo em minutos: ")

    velocidade = calcular_velocidade(distancia, tempo)

    if velocidade is None:
        print("Tempo não pode ser zero. Velocidade indefinida.")
    else:
        print(f"Velocidade: {velocidade:.2f} m/s")


if __name__ == "__main__":
    main()
