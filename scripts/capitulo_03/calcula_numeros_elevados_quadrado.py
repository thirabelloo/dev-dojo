"""Calcula e exibe os quadrados dos números em um intervalo definido pelo usuário."""


def obter_numero(mensagem):
    """Solicita ao usuário um número inteiro positivo.

    Args:
        mensagem: Texto exibido ao solicitar a entrada.

    Returns:
        Um número inteiro maior que zero.
    """

    while True:
        try:
            numero = int(input(mensagem))
            if numero > 0:
                return numero
            print("O número deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def validar_intervalos(inicio, fim):
    """Verifica se o intervalo é válido.

    Args:
        inicio: Número inicial.
        fim: Número final.

    Raises:
        ValueError: Se o número inicial for maior que o final.
    """

    if inicio > fim:
        raise ValueError("O número inicial não pode ser maior que o final.")


def eleva_ao_quadrado(numero_inicial, numero_final):
    """Calcula os quadrados dos números no intervalo.

    Args:
        numero_inicial: Início do intervalo.
        numero_final: Fim do intervalo.

    Returns:
        Lista com os quadrados dos números.
    """

    return [i**2 for i in range(numero_inicial, numero_final + 1)]


def exibir_resultados(valores, numero_inicial):
    """Exibe os resultados formatados no terminal.

    Args:
        valores: Lista de quadrados.
        numero_inicial: Número inicial usado como base.
    """

    print(
        f"\nQuadrados dos números de {numero_inicial} até {numero_inicial + len(valores) - 1}:\n"
    )
    for i, valor in enumerate(valores, start=numero_inicial):
        print(f"{i}² = {valor}")


def main():
    """Executa o fluxo principal do programa."""

    try:
        x = obter_numero("Digite o número inicial: ")
        y = obter_numero("Digite o número final: ")
        validar_intervalos(x, y)
        resultado = eleva_ao_quadrado(numero_inicial=x, numero_final=y)
        exibir_resultados(resultado, x)
    except ValueError as e:
        print(f"\nErro: {e}")
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")


if __name__ == "__main__":
    main()
