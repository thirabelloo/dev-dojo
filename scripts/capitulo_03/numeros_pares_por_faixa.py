"""Solicita um intervalo de números inteiros positivos e exibe os pares contidos nele."""


def coletar_numero(mensagem):
    """
    Solicita ao usuário um número inteiro maior ou igual a zero.

    Args:
        mensagem (str): Texto exibido ao solicitar a entrada.

    Returns:
        int: Número inteiro fornecido pelo usuário.
    """

    while True:
        try:
            valor = int(input(mensagem))
            if valor >= 0:
                return valor
            print("Digite um número maior ou igual a zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def validar_intervalos(valor_inicial, valor_final):
    """
    Verifica se o intervalo fornecido é válido.

    Args:
        valor_inicial (int): Número inicial.
        valor_final (int): Número final.

    Raises:
        ValueError: Se o número inicial for maior que o número final.
    """
    if valor_inicial > valor_final:
        raise ValueError("O número inicial não pode ser maior que o número final.")


def calcular_pares(inicio, fim):
    """
    Retorna uma lista com todos os números pares dentro do intervalo fornecido.

    Args:
        inicio (int): Início do intervalo.
        fim (int): Fim do intervalo.

    Returns:
        list: Lista contendo os números pares no intervalo.
    """

    return [num for num in range(inicio, fim + 1) if num % 2 == 0]


def exibir_resultado(pares, inicio, fim):
    """
    Exibe os números pares encontrados.

    Args:
        pares (list): Lista de números pares.
        inicio (int): Limite inferior do intervalo.
        fim (int): Limite superior do intervalo.
    """

    print(f"\nNúmeros pares entre {inicio} e {fim}:")
    print(", ".join(map(str, pares)) if pares else "Nenhum número par encontrado.")


def main():
    """
    Executa o fluxo principal do programa.
    """
    print("🔢 Identificador de Números Pares")
    print(
        "Este programa exibe todos os números pares dentro de um intervalo definido por você.\n"
    )
    try:
        limite_inicial = coletar_numero("Digite o número inicial do intervalo: ")
        limite_final = coletar_numero("Digite o número final do intervalo: ")
        validar_intervalos(limite_inicial, limite_final)
        pares_encontrados = calcular_pares(limite_inicial, limite_final)
        exibir_resultado(pares_encontrados, limite_inicial, limite_final)
    except ValueError as e:
        print(f"\nErro de intervalo: {e}")
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário. Até a próxima!")


if __name__ == "__main__":
    main()
