"""
Script para calcular o salário base e líquido de um funcionário.

Este programa solicita ao usuário o valor do salário bruto, calcula os descontos aplicáveis,
e apresenta o salário líquido após os descontos.

Funções principais:
- calcular_salario_base: Calcula o salário base a partir das horas trabalhadas e valor por hora.
- calcular_total_desconto: Calcula o valor total dos descontos sobre o salário base.
- calcular_salario_liquido: Calcula o salário líquido após descontos.
- entrada_usuario: Solicita e valida entradas do usuário.
- main: Orquestra o fluxo do programa.
"""


def calcular_salario_base(horas_trabalhadas, valor_hora):
    """
    Calcula o salário base com base nas horas trabalhadas e no valor por hora.

    Parameters:
        horas_trabalhadas (float): Quantidade de horas trabalhadas no mês.
        valor_hora (float): Valor monetário recebido por hora.

    Returns:
        float: Salário base calculado.
    """

    return horas_trabalhadas * valor_hora


def calcular_total_desconto(salario_base, percentual_desconto):
    """
    Calcula o valor total de desconto aplicado sobre o salário base.

    Parameters:
        salario_base (float): Valor do salário antes dos descontos.
        percentual_desconto (float): Percentual de desconto a ser aplicado (0 a 100).

    Returns:
        float: Valor total de desconto.

    Raises:
        ValueError: Se o salário base for negativo.
    """

    if salario_base < 0:
        raise ValueError("Salário base não pode ser negativo.")
    return (percentual_desconto / 100) * salario_base


def calcular_salario_liquido(salario_base, total_desconto):
    """
    Calcula o salário líquido após aplicação dos descontos.

    Parameters:
        salario_base (float): Valor do salário antes dos descontos.
        total_desconto (float): Valor total de desconto aplicado.

    Returns:
        float: Salário líquido após os descontos.

    Raises:
        ValueError: Se o desconto exceder o salário base.
    """

    if total_desconto > salario_base:
        raise ValueError("Desconto não pode exceder o salário base.")
    return salario_base - total_desconto


def entrada_usuario(mensagem, nome_regra, valor_minimo, valor_maximo):
    """
    Solicita um valor numérico ao usuário, validando se está dentro do intervalo permitido.

    Parameters:
        mensagem (str): Texto exibido ao solicitar o valor.
        nome_regra (str): Nome do campo para exibição em mensagens de erro.
        valor_minimo (float): Valor mínimo permitido.
        valor_maximo (float): Valor máximo permitido.

    Returns:
        float: Valor numérico validado inserido pelo usuário.
    """

    while True:
        input_usuario = input(mensagem)
        try:
            valor = float(input_usuario)
            if not valor_minimo <= valor <= valor_maximo:
                print(
                    f"Erro: '{nome_regra}' deve estar entre {valor_minimo} e {valor_maximo}."
                )
                continue
            return valor
        except ValueError:
            print(f"Erro: Valor inválido para '{nome_regra}'.")


def main():
    """
    Executa o fluxo principal da calculadora de salário mensal.

    Solicita os dados ao usuário, realiza os cálculos e exibe os resultados.
    """

    print("🧮 Calculadora de Salário Mensal\n")

    horas_trabalhadas = entrada_usuario(
        "🕒 Horas trabalhadas no mês: ", "horas trabalhadas", 0, 260
    )
    valor_hora = entrada_usuario("💰 Valor por hora (R$): ", "valor por hora", 0, 500)
    percentual_desconto = entrada_usuario(
        "📉 Percentual de desconto (0 a 100): ", "percentual de desconto", 0, 100
    )

    try:
        salario_base = calcular_salario_base(horas_trabalhadas, valor_hora)
        total_desconto = calcular_total_desconto(salario_base, percentual_desconto)
        salario_liquido = calcular_salario_liquido(salario_base, total_desconto)

        print("\n📊 Resultado do cálculo:")
        print(f"➡ Salário Base: R$ {salario_base:.2f}")
        print(f"➡ Total de Descontos: R$ {total_desconto:.2f}")
        print(f"✅ Salário Líquido: R$ {salario_liquido:.2f}")

    except ValueError as erro:
        print(f"\nErro de valor: {erro}")
    except TypeError as erro:
        print(f"\nErro de tipo: {erro}")


if __name__ == "__main__":
    main()
