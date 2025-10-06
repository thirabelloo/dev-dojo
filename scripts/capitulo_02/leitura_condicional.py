"""
Programa que verifica se um número inteiro informado está dentro do intervalo permitido (1 a 9).
"""


def obter_numero_inteiro():
    """
    Solicita ao usuário um número inteiro, validando a entrada.

    Returns:
        int: Número inteiro informado pelo usuário.
    """

    while True:
        try:
            return int(input("Informe um número inteiro: "))
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar apenas números inteiros.")


def verificar_intervalo_valido(valor):
    """
    Verifica se o número está entre 1 e 9 (inclusive).

    Args:
        numero (int): Número a ser avaliado.

    Returns:
        str: Mensagem indicando se está dentro ou fora do intervalo permitido.
    """

    if 1 <= valor <= 9:
        return "O número está dentro do intervalo permitido (1 a 9)."
    return "O número está fora do intervalo permitido. Tente um valor entre 1 e 9."


def main():
    """
    Função principal que coordena a execução do programa.
    """

    numero_informado = obter_numero_inteiro()
    resultado = verificar_intervalo_valido(numero_informado)
    print(resultado)


if __name__ == "__main__":
    main()
