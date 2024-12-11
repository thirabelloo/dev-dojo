"Script que retorna uma lista de números pares no intervalo especificado "


def listar_numeros_pares(numero_inicial, numero_final):
    """
    Retorna uma lista de números pares no intervalo especificado.

    Args:
        numero_inicial (int): O número inicial do intervalo.
        numero_final (int): O número final do intervalo.

    Raises:
        ValueError: Se as entradas não forem inteiros ou se o número inicial for maior que o número final.

    Returns:
        list: Lista de números pares no intervalo especificado.
    """

    if not isinstance(numero_inicial, int) or not isinstance(numero_final, int):
        raise ValueError("As entradas devem ser números inteiros.")

    if numero_inicial > numero_final:
        raise ValueError("O número inicial deve ser menor ou igual ao número final.")

    lista_pares = [i for i in range(numero_inicial, numero_final + 1) if i % 2 == 0]
    return lista_pares


# Faixa determinada no exercicio
print(listar_numeros_pares(0, 100))
