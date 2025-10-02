"""
Calculadora de Vizinhos Numéricos

Este script solicita ao usuário um número inteiro e exibe seu antecessor e sucessor.
Ideal para fins educativos ou demonstrações simples de entrada, processamento e saída em Python.
"""


def coletar_numero(mensagem):
    """
    Solicita ao usuário a entrada de um número inteiro.

    Parameters:
        mensagem (str): Texto exibido ao usuário solicitando a entrada.

    Returns:
        int: Número inteiro digitado pelo usuário.
    """

    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida. Digite um valor numérico.")


def calcula_vizinhos(numero):
    """
    Calcula o antecessor e o sucessor de um número inteiro.

    Parameters:
        numero (int): Número base para o cálculo.

    Returns:
        tuple: Tupla contendo o antecessor e o sucessor do número.
    """

    return numero - 1, numero + 1


def exibir_resultado(numero, antecessor, sucessor):
    """
    Exibe o número digitado, seu antecessor e seu sucessor formatados no console.

    Parameters:
        numero (int): Número digitado pelo usuário.
        antecessor (int): Número imediatamente anterior.
        sucessor (int): Número imediatamente posterior.
    """

    print("\n📊 Resultado:")
    print(f"🔢 Número digitado: {numero}")
    print(f"⬅️ Antecessor: {antecessor}")
    print(f"➡️ Sucessor: {sucessor}")


def main():
    """
    Função principal que coordena a execução do programa:
    coleta o número do usuário, calcula os vizinhos e exibe o resultado.
    """

    numero = coletar_numero(
        "Digite um número para descobrir seu antecessor e sucessor: "
    )
    numero_antecessor, numero_sucessor = calcula_vizinhos(numero)
    exibir_resultado(numero, numero_antecessor, numero_sucessor)


if __name__ == "__main__":
    main()
