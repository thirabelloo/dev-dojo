"""Script que cálcula de quantos litros de combustível um automóvel consome em uma viagem """


def calcula_litros_combustivel(tempo_gasto, velocidade):
    """
    Calcula a quantidade de litros de combustível consumidos em uma viagem.

    Parâmetros:
    tempo_gasto (float): Tempo gasto na viagem em horas.
    velocidade (float): Velocidade média do automóvel em km/h.

    Retorna:
    float: A quantidade de litros de combustível consumidos, formatada com duas casas decimais.
    """
    autonomia_automovel = 12
    if not isinstance(velocidade, (int, float)) or not isinstance(
        tempo_gasto, (int, float)
    ):
        raise TypeError("O tempo gasto e a velocidade devem ser números")
    distancia = tempo_gasto * velocidade

    litros_utilizacao = distancia / autonomia_automovel
    return f"Total de litros gastos: {litros_utilizacao:.2f} litros"
