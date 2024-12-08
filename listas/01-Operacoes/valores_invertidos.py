"""Script que trocar os valores das variáveis e apresentar o resultado dos valores invertidos"""


def valores_invertido(x, y):
    """
    Lê os valores para as variáveis x e y, troca os valores das variáveis
    e apresenta o resultado dos valores invertidos.

    Parâmetros:
        x (int, float): O valor da variável x. Deve ser um número.
        y (int, float): O valor da variável y. Deve ser um número.

    Retorna:
        Nenhum: A função imprime os valores invertidos de x e y.
        Se os valores fornecidos não forem números, uma exceção TypeError será lançada.
    """

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("X e Y devem ser números")

    print(f"Os valores digitado para x= {x} e para y= {y}")
    x, y = y, x
    print(f"Os valores invertidos sao x= {x}, y = {y}")
