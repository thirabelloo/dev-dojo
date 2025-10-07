"""
Módulo de geração de tabuada interativa.

Solicita ao usuário um número inteiro positivo e exibe sua tabuada até um limite superior.
Ideal para fins educacionais ou prática de estruturas de repetição.
"""


def solicitar_numero():
    """
    Solicita ao usuário um número inteiro positivo.

    Retorna:
        int: O número digitado pelo usuário, garantidamente maior ou igual a zero.
    """

    while True:
        try:
            numero_base = int(input("Digite um número inteiro positivo: "))
            if numero_base >= 0:
                return numero_base
            print("O número deve ser maior ou igual a zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def calcular_tabuada(numero_base, limite=10):
    """
    Exibe a tabuada do número fornecido até o limite especificado.

    Parâmetros:
        numero_base (int): O número para o qual a tabuada será gerada.
        limite_superior (int, opcional): O valor final da tabuada. Padrão é 10.

    Retorna:
        None
    """
    print(f"\nTabuada do {numero_base}:\n")
    for i in range(1, limite + 1):
        print(f"{i} * {numero_base} = {i * numero_base}")


def main():
    """
    Função principal que coordena a execução do programa.

    Solicita um número ao usuário e exibe sua tabuada.
    """

    numero_base = solicitar_numero()
    calcular_tabuada(numero_base)


if __name__ == "__main__":
    main()
