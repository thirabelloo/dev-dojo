""" Lê um número inteiro fornecido pelo usuário, calcula seu antecessor e sucessor, e exibe os resultados. """


def calcula_antecessor_sucessor():
    """
    Solicita um número inteiro ao usuário, calcula o antecessor e o sucessor do número fornecido, e exibe os resultados.
    Retorna: None: Esta função não retorna nenhum valor. Os resultados são impressos"""
    try:
        numero = int(input("Digite o numero:"))
    except ValueError:
        print("Error: Entrada inválida. Por favor, digite um número inteiro.")
        return

    numero_antecessor = numero - 1
    numero_sucessor = numero + 1

    print(
        f"Numero antecessor: {numero_antecessor}\n"
        f"Número digitado: {numero}\n"
        f"Número sucessor: {numero_sucessor}\n"
    )
