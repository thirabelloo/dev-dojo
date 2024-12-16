"""Script que calcula a sequência de Fibonacci"""


def valida_entrada_fibonacci():
    """
    Solicita ao usuário a quantidade de termos da sequência de Fibonacci que deseja gerar.
    Valida se a entrada é um número inteiro maior que 0.

    Returns:
        int: O número de termos da sequência de Fibonacci solicitado pelo usuário.
    """
    try:
        numero_fibonacci_usuario = int(
            input("Quantos termos da sequência de Fibonacci você deseja? ")
        )

        if numero_fibonacci_usuario <= 0:
            raise ValueError("Erro: o número deve ser maior que 0.")
        return numero_fibonacci_usuario
    except ValueError:
        print("Erro: As entradas devem ser números inteiros.")
    return valida_entrada_fibonacci()


def calcula_fibonacci(numero_termos):
    """
    Calcula e exibe a sequência de Fibonacci até o número de termos especificado.
    Args:
        numero_termos (int): O número de termos da sequência de Fibonacci a serem gerados.
    """
    fibonacci_sequencia = [0, 1]
    while len(fibonacci_sequencia) < numero_termos:
        fibonacci = fibonacci_sequencia[-1] + fibonacci_sequencia[-2]
        fibonacci_sequencia.append(fibonacci)

    print(f"Sequência de Fibonacci até o {numero_termos}º termo:")
    for i, valor_gerado in enumerate(fibonacci_sequencia):
        print(f"Termo {i+1}: {valor_gerado}")


def main():
    """
    Função principal que gerencia o fluxo do programa.
    Solicita a entrada do usuário e calcula a sequência de Fibonacci.
    """
    entrada = valida_entrada_fibonacci()
    return calcula_fibonacci(entrada)


main()
