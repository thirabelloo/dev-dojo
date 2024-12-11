"""Script que presente os quadrados dos números inteiros existentes na faixa de valores de 15 até 200"""


def calcular_quadrados_por_faixa(numero_inicial, numero_final):
    """
    Calcula os quadrados dos números inteiros em uma faixa específica.

    Args:
        numero_inicial (int): O número inicial da faixa.
        numero_final (int): O número final da faixa.

    Returns:
        list: Uma lista contendo os quadrados dos números na faixa de numero_inicial a numero_final.

    Raises:
        ValueError: Se as entradas não forem números inteiros ou se o número inicial for maior que o número final.
    """

    if not isinstance(numero_inicial, int) or not isinstance(numero_final, int):
        raise ValueError("Erro: As entradas devem ser números inteiros.")

    if numero_inicial > numero_final:
        raise ValueError(
            "Erro: O número inicial deve ser menor ou igual ao número final."
        )

    lista = [i**2 for i in range(numero_inicial, numero_final + 1)]
    return lista


# Faixa determinada no exercicio
print(calcular_quadrados_por_faixa(15, 200))
