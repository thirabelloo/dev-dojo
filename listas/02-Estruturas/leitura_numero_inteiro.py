"""Script que executa a leitura de um valor numérico inteiro, caso o valor esteja entre 1 e 9 apresentar a mensagem"""


def obter_numero_usuario():
    """
    Solicita ao usuário que insira um número inteiro.

    Returns:
        int: O número inteiro inserido pelo usuário.
    """
    while True:
        try:
            valor = int(input("Digite um número: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")


def valida_numero(numero):
    """
    Verifica se o número está dentro do intervalo permitido.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        str: Mensagem indicando se o número está dentro ou fora do valor permitido.
    """
    if 1 <= numero <= 9:
        return "Dentro do valor permitido"
    return "Fora do valor permitido"


def main():
    """
    Função principal que lê um número do usuário, valida-o e imprime o resultado.
    """
    numero = obter_numero_usuario()
    resultado = valida_numero(numero)
    print(resultado)
