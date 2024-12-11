"""Script que apresenta o somatório dos números na faixa especificada."""


def somatorio_numeros_por_faixa(numero_inicial, numero_final):
    """
    Calcula a soma dos números inteiros dentro de uma faixa especificada.

    Args:
        numero_inicial (int): O primeiro número da faixa.
        numero_final (int): O último número da faixa.

    Raises:
        ValueError: Se as entradas não forem inteiras ou se o número inicial for maior que o número final.

    Returns:
        str: Uma string informando a soma dos números na faixa.
    """
    if not isinstance(numero_inicial, int) or not isinstance(numero_final, int):
        raise ValueError("As entradas devem ser números inteiros.")

    if numero_inicial > numero_final:
        raise ValueError(
            "Erro: O número inicial deve ser menor ou igual ao número final."
        )

    soma = sum(range(numero_inicial, numero_final + 1))
    return f"A somatória de {numero_inicial} até {numero_final} é igual a {soma}"


# Faixa determinada no exercicio
print(somatorio_numeros_por_faixa(1, 500))
