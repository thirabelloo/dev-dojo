"""Script que calcula o IMC e gere uma classificacao de acordo com seu IMC"""


def obter_peso_altura():
    """
    Recebe a altura e o peso do usuário através de entrada de dados.

    Solicita repetidamente a altura e o peso até que valores válidos sejam inseridos.
    A altura deve estar entre 0.5 e 2.5 metros, e o peso entre 1 e 300 quilogramas.

    Returns:
        tuple: A altura (em metros) e o peso (em quilogramas) do usuário.
    """
    while True:
        try:
            altura = float(input("Digite a sua altura em metros(m): "))
            peso = float(input("Digite o seu peso em quilogramas(kg): "))
            if not 0.5 <= altura <= 2.5:
                print("Por favor, insira uma altura válida entre 0.5 e 2.5 metros.")
            elif not 1 <= peso <= 300:
                print("Por favor, insira um peso válido entre 1 e 300 quilogramas.")
            else:
                return altura, peso
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def calcula_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos.
    Calcula o IMC utilizando a fórmula IMC = peso / altura^2.
    Se a altura for igual a zero, uma exceção ZeroDivisionError é levantada.

    Args:
        peso (float): O peso em quilogramas.
        altura (float): A altura em metros.

    Returns:
        float: O valor do IMC.

    Raises:
        ZeroDivisionError: Se a altura for igual a zero.
    """
    if altura == 0:
        raise ZeroDivisionError("A altura não pode ser zero.")
    return peso / (altura**2)


def status_imc(imc):
    """
    Determina a classificação do IMC baseado no valor calculado.
    Classifica o status do IMC em categorias como "NORMAL", "OBESIDADE GRAU I", etc.
    com base no valor do IMC fornecido.

    Args:
        imc (float): O valor do IMC.

    Returns:
        str: O status do IMC do usuário.
    """
    classificacoes = {
        "DESNUTRICAO GRAU V": (0, 9.9),
        "DESNUTRICAO GRAU IV": (10, 12.9),
        "DESNUTRICAO GRAU III": (13, 15.9),
        "DESNUTRICAO GRAU II": (16, 16.9),
        "DESNUTRICAO GRAU I": (17, 18.4),
        "NORMAL": (18.5, 24.9),
        "PRE-OBESIDADE": (25, 29.9),
        "OBESIDADE GRAU I": (30, 34.5),
        "OBESIDADE GRAU II": (35, 39.9),
        "OBESIDADE GRAU III": (40, float("inf")),
    }

    for classificao, (min_valor, max_valor) in classificacoes.items():
        if min_valor <= imc <= max_valor:
            return classificao
    return "VALOR INVALIDO"


def main():
    """
    Determina o status do IMC baseado na média das notas.

    Args:
        imc (float): O valor do IMC.

    Returns:
        str: O status do IMC do usuário.
    """
    try:
        altura, peso = obter_peso_altura()
        resultado_imc = calcula_imc(peso, altura)
        resultado_status_imc = status_imc(resultado_imc)
        print(
            f"O cálculo do seu IMC é: {resultado_imc:.2f} e a classificação do seu IMC é: {resultado_status_imc}"
        )
    except ValueError as error:
        print(f"Erro: {error}")
    except ZeroDivisionError as error:
        print(f"Erro: {error}")


main()
