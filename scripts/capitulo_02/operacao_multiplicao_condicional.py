"""
Programa que solicita um número inteiro ao usuário,
multiplica esse número por um fator fixo e exibe o resultado
apenas se ele for maior ou igual a 30.
"""

# Constantes de regra de negócio
FATOR_MULTIPLICACAO = 2
LIMITE_EXIBICAO = 30


def obter_numero_inteiro():
    """
    Solicita ao usuário um número inteiro, validando a entrada.

    Returns:
        int: Número inteiro informado pelo usuário.
    """

    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar apenas números inteiros.")


def calcular_multiplicacao(numero):
    """
    Multiplica o número pelo fator definido e retorna uma mensagem
    apenas se o resultado for maior ou igual ao limite de exibição.

    Args:
        numero (int): Número a ser multiplicado.

    Returns:
        str: Mensagem com o resultado ou aviso de valor insuficiente.
    """

    resultado = numero * FATOR_MULTIPLICACAO
    if resultado >= LIMITE_EXIBICAO:
        return f"O resultado da multiplicação por {FATOR_MULTIPLICACAO} é: {resultado}"
    return f"O resultado ({resultado}) é menor que o limite mínimo de {LIMITE_EXIBICAO} e não será exibido."


def main():
    """
    Função principal que coordena a execução do programa.
    """

    valor = obter_numero_inteiro()
    resultado = calcular_multiplicacao(valor)
    print(resultado)


if __name__ == "__main__":
    main()
