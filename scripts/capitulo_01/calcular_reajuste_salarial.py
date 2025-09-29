"""
Calculadora de reajuste salarial.

Este script coleta o salário base e o percentual de reajuste informados pelo usuário,
calcula o novo salário e exibe os valores de reajuste e salário atualizado.
"""


def calcular_novo_salario(salario_base, percentual_reajuste):
    """
    Calcula o novo salário após aplicar o percentual de reajuste.

    Args:
        salario_base (float): Valor atual do salário.
        percentual_reajuste (float): Percentual de aumento a ser aplicado.

    Returns:
        float: Novo salário com reajuste aplicado, arredondado para duas casas decimais.
    """
    reajuste = calcular_reajuste(salario_base, percentual_reajuste)
    return round(salario_base + reajuste, 2)


def calcular_reajuste(salario, percentual):
    """
    Calcula o valor do reajuste com base no salário e percentual informado.

    Args:
        salario (float): Valor atual do salário.
        percentual (float): Percentual de reajuste.

    Returns:
        float: Valor do reajuste, arredondado para duas casas decimais.
    """
    return round(salario * (percentual / 100), 2)


def coletar_informacoes(texto):
    """
    Solicita ao usuário uma entrada numérica maior que zero.

    Args:
        texto (str): Mensagem exibida ao usuário no prompt de entrada.

    Returns:
        float: Valor numérico válido informado pelo usuário.
    """
    while True:
        try:
            valor = float(input(texto))
            if valor > 0:
                return valor
            print("O valor deve ser maior que zero. Tente novamente!")
        except ValueError:
            print("Entrada inválida: Digite um número válido.")


def main():
    """
    Função principal que executa a calculadora de reajuste salarial.

    Coleta os dados do usuário, calcula o novo salário e exibe os resultados.
    """
    print("\n📆 Calculadora de reajuste salarial")
    salario_base = coletar_informacoes("Informe o salário base (R$): ")
    percentual_reajuste = coletar_informacoes("Informe o percentual de reajuste (%): ")
    novo_salario = calcular_novo_salario(salario_base, percentual_reajuste)
    print(f"\n🔧 Valor do reajuste: R$ {round(novo_salario - salario_base, 2)}")
    print(f"💰 Novo salário após reajuste: R$ {novo_salario}")


if __name__ == "__main__":
    main()
