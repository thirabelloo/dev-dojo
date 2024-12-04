"""Script que ler o salário base mensal de um funcionário e o percentual de reajuste e calcula o novo valor de salário do funcionário"""


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
        raise TypeError(f"{nome} tem que ser um número")


def novo_salario(salario_base, percentual_de_reajuste):
    """
    Calcula o novo salário de um funcionário com base no salário base e no percentual de reajuste.

    Parâmetros:
    salario_base (int, float): O salário base mensal do funcionário. Deve ser um número.
    percentual_de_reajuste (int, float): O percentual de reajuste aplicado ao salário. Deve ser um número.

    Retorna:
    str: Uma string formatada com o novo valor do salário do funcionário.
    """
    for nomes, valores in [
        ("Salario Base", salario_base),
        ("Percentual de Reajuste", percentual_de_reajuste),
    ]:
        valida_tipo_variavel(nomes, valores)

    calculo_novo_salario = salario_base + (salario_base * percentual_de_reajuste) / 100
    return f"O novo salário é de R$ {calculo_novo_salario:.2f} "
