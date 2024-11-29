"""Script que calcule o salário líquido de um funcionário"""


def calcula_salario_funcionarios(
    horas_trabalhadas, valor_hora_trabalho, percentual_desconto
):
    """
    Calcula o salário líquido de um funcionário.

    Parâmetros:
    horas_trabalhadas (float): Horas trabalhadas.
    valor_hora_trabalho (float): Valor da hora de trabalho.
    percentual_desconto (float): Percentual de desconto.

    Retorna:
    dict: Um dicionário contendo o salário base e o salário líquido formatados com duas casas decimais.
    """
    try:
        if horas_trabalhadas < 0 or valor_hora_trabalho < 0 or percentual_desconto < 0:
            raise ValueError(
                "Horas trabalhadas, valor da hora e percentual de desconto devem ser numeros positivos."
            )
        salario_base = horas_trabalhadas * valor_hora_trabalho
        total_desconto = (percentual_desconto / 100) * salario_base
        salario_liquido = salario_base - total_desconto
        return {
            "Salario Base R$": f"{salario_base: .2f}",
            "Salario Liquido R$": f"{salario_liquido: .2f}",
        }
    except TypeError:
        return "Os Valores de horas trabalhadas, valor da hora e percentual de desconto devem ser numeros."
    except ValueError as ve:
        return str(ve)
