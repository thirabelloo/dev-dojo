"""Gera e exibe os primeiros termos da sequência de Fibonacci com base na entrada do usuário."""


def coletar_numero(mensagem):
    """
    Solicita ao usuário um número inteiro maior que zero.

    Args:
        mensagem (str): Texto exibido ao solicitar a entrada.

    Returns:
        int: Número inteiro positivo fornecido pelo usuário.
    """

    while True:
        try:
            termo = int(input(mensagem))
            if termo > 0:
                return termo
            print("Por favor, digite um número maior que zero.")

        except ValueError:
            print("Entrada inválida. Digite apenas número inteiro.")


def gerar_sequencia_fibonacci(quantidade):
    """
    Gera os primeiros 'quantidade' termos da sequência de Fibonacci.

    Args:
        quantidade (int): Número de termos a serem gerados.

    Yields:
        int: Próximo número da sequência de Fibonacci.
    """

    a, b = 0, 1
    for _ in range(quantidade):
        yield a
        a, b = b, a + b


def main():
    """
    Função principal que executa o gerador de sequência de Fibonacci.
    """

    print("🔢 Gerador de Sequência de Fibonacci")
    quantidade = coletar_numero(
        "Digite a quantidade de termos da sequência de Fibonacci: "
    )
    sequencia = list(gerar_sequencia_fibonacci(quantidade))
    print(f"\n📈 Sequência de Fibonacci com {quantidade} termo(s):")
    print(", ".join(map(str, sequencia)))


if __name__ == "__main__":
    main()
