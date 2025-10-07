"""
Este módulo solicita ao usuário um intervalo de números inteiros positivos
e calcula o somatório dos números dentro desse intervalo.
"""


def coletar_numero(mensagem):
    """Solicita ao usuário um número inteiro positivo.

    Args:
        mensagem (str): Texto exibido ao solicitar a entrada.

    Returns:
        int: Um número inteiro maior que zero.
    """

    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros")


def validar_intervalos(inicio, fim):
    """Verifica se o intervalo é válido.

    Args:
        inicio: Número inicial.
        fim: Número final.

    Raises:
        ValueError: Se o número inicial for maior que o final.
    """

    if inicio > fim:
        raise ValueError("O número inicial não pode ser maior que o número final.")


def somatoria(numero_inicial, numero_final):
    """Calcula o somatório dos números no intervalo.

    Args:
        numero_inicial (int): Início do intervalo.
        numero_final (int): Fim do intervalo.

    Returns:
        int: Somatório dos números entre número_inicial e número_final.
    """

    return sum(range(numero_inicial, numero_final + 1))


def main():
    """Executa o fluxo principal do programa."""
    print("📊 Calculadora de Somatório")
    print("Informe dois números positivos para definir o intervalo.\n")

    try:
        x = coletar_numero("Digite o número inicial: ")
        y = coletar_numero("Digite o número final: ")

        validar_intervalos(x, y)
        resultado = somatoria(numero_inicial=x, numero_final=y)
        print(f"\n✅  O somatório dos números de {x} até {y} é: {resultado}")
    except ValueError as e:
        print(f"\nErro: {e}")
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")


if __name__ == "__main__":
    main()
