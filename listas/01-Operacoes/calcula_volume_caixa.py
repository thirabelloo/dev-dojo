"""Script que calcula o volume de uma caixa retangular """


def valida_tipo_variavel(nome, variavel):
    """
    Valida se uma variável é do tipo int ou float.

    Parâmetros:
    nome (str): O nome da variável para exibir na mensagem de erro.
    variavel (int, float): O valor a ser validado.

    Retorna:
    Nenhum: Lança TypeError se o valor não for int ou float.
    """
    if not isinstance(variavel, (int, float)):
        raise TypeError(f"{nome} deve ser um numero")


def calcula_volume_caixa_retangular(comprimento, largura, altura):
    """
    Calcula o volume de uma caixa retangular.

    Parâmetros:
        comprimento (int, float): O comprimento da caixa. Deve ser um número.
        largura (int, float): A largura da caixa. Deve ser um número.
        altura (int, float): A altura da caixa. Deve ser um número.

    Retorna: 
        str: O volume da caixa retangular formatado em cm³.
    """
    for nomes, valores in [
        ("Comprimento", comprimento),
        ("Largura", largura),
        ("Altura", altura),
    ]:
        valida_tipo_variavel(nomes, valores)
    volume = comprimento * largura * altura

    return f"O Volume da caixa é de {volume:.2f}cm³"
