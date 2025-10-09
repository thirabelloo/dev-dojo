"""Módulo para cálculo de fatorial de números inteiros não-negativos."""

from math import factorial


def coletar_numero(mensagem):
    """
    Solicita ao usuário um número inteiro não-negativo.

    Args:
        mensagem (str): Texto exibido ao solicitar a entrada.

    Returns:
        int: Número inteiro não-negativo informado pelo usuário.
    """

    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print(
                    "Erro: o número deve ser um inteiro não-negativo. Tente novamente."
                )
            else:
                return valor
        except ValueError:
            print("Entrada inválida: por favor, digite apenas números inteiros.")


def calcular_fatorial(numero):
    """
    Calcula o fatorial de um número inteiro.

    Args:
        numero (int): Número inteiro não-negativo.

    Returns:
        int: Resultado do fatorial.
    """

    return factorial(numero)


def main():
    """
    Função principal que executa o fluxo de cálculo de fatorial.
    """

    print("📊 Cálculo de Fatorial")
    numero_usuario = coletar_numero("Informe um número inteiro não-negativo: ")
    resultado_fatorial = calcular_fatorial(numero_usuario)
    print(f"Resultado: o fatorial de {numero_usuario} é {resultado_fatorial}")


if __name__ == "__main__":
    main()
