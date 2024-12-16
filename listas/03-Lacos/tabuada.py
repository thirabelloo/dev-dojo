"""Script que calcula e apresenta a tabuada de um número qualquer."""


def validacao_entrada():
    """
    Solicita ao usuário um número inteiro não negativo e valida a entrada.

    Retorna:
        int: O número validado fornecido pelo usuário.
    """
    try:
        numero = int(input("Digite o número que deseja saber a tabuada: "))
        if numero < 0:
            raise ValueError("Erro: Digite um número maior ou igual ao zero.")
        return numero
    except ValueError:
        print(("Erro: Digite um número inteiro."))
        return validacao_entrada()


def tabuada():
    """
    Calcula e exibe a tabuada de um número fornecido pelo usuário.

    A função solicita ao usuário um número inteiro não negativo, e então calcula e imprime
    a tabuada desse número de 0 a 10.
    """
    numero_entrada = validacao_entrada()
    for i in range(0, 11):
        print(f"{i} * {numero_entrada} = {i * numero_entrada}")


tabuada()
