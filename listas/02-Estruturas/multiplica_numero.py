"""Script que ler um número inteiro qualquer e multiplica por 2"""


def obter_numeros_usuario():
    """
    Solicita ao usuário a entrada de um número inteiro positivo.

    Retorna:
        int: O número inteiro positivo fornecido pelo usuário.
    """
    while True:
        try:
            valor = int(input("Digite o número: "))
            if valor <= 0:
                print("Erro: Por favor, insira um número maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def multiplicacao_numeracao(numero, multiplicador):
    """
    Multiplica o número fornecido pelo multiplicador e retorna o resultado se for maior ou igual a 30.

    Parâmetros:
        numero (int): O número a ser multiplicado.
        multiplicador (int): O fator pelo qual o número será multiplicado.

    Retorna:
    str: Uma mensagem com o resultado da multiplicação ou indicando que o resultado não atingiu o valor.
    """
    resultado = numero * multiplicador

    if resultado >= 30:
        return f"O resultado é {resultado}"

    return "O resultado não atingiu o valor."


def main():
    """
    Função principal que obtém um número do usuário, realiza a multiplicação e exibe o resultado.
    """
    entrada_input = obter_numeros_usuario()
    multiplicador = 2
    resultado = multiplicacao_numeracao(entrada_input, multiplicador)
    print(resultado)
