"""
Script de operações numéricas básicas.
Permite ao usuário inserir dois números e exibe os resultados de adição, subtração, multiplicação e divisão.
"""


def coletar_numeros(mensagem):
    """
    Solicita ao usuário um número (float) com validação de entrada.

    Args:
        mensagem (str): Texto exibido ao solicitar o número.

    Returns:
        float: Número fornecido pelo usuário.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


def calcular_operacoes(a, b):
    """
    Calcula as quatro operações aritméticas básicas entre dois números.

    Args:
        a (float): Primeiro número.
        b (float): Segundo número.

    Returns:
        dict: Resultados das operações com tratamento para divisão por zero.
    """

    resultados = {
        "Adição": a + b,
        "Subtração": a - b,
        "Multiplicação": a * b,
        "Divisão": a / b if b != 0 else None,
    }
    return resultados


def exibir_resultado(resultados):
    """
    Exibe os resultados das operações aritméticas.

    Args:
        resultados (dict): Dicionário com os resultados das operações.
    """

    print("\n📊 Resultados das operações:")
    for operacao, resultado in resultados.items():
        if resultado is None:
            print(f"{operacao}: Indefinida (divisão por zero)")
        else:
            print(f"{operacao}: {resultado}")


def main():
    """
    Função principal que coordena a coleta de dados, cálculo e exibição dos resultados.
    """

    numero_1 = coletar_numeros("Digite o valor do primeiro número: ")
    numero_2 = coletar_numeros("Digite o valor do segundo número: ")
    resultados = calcular_operacoes(numero_1, numero_2)
    exibir_resultado(resultados)


if __name__ == "__main__":
    main()
