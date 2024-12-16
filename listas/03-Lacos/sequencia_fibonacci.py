"""Script que calcula a sequência de Fibonacci até o décimo quinto termo."""


def calcula_fibonacci():
    """
    Calcula e apresenta a sequência de Fibonacci até o décimo quinto termo.

    A sequência de Fibonacci é uma série de números na qual cada número é
    a soma dos dois precedentes, começando por 0 e 1. Este programa calcula
    e imprime os primeiros 15 termos da sequência.

    Returns:
        None
    """
    numero_termos = 15  # Número fixo de termos para a sequência de Fibonacci
    fibonacci_sequencia = [0, 1]
    while len(fibonacci_sequencia) < numero_termos:
        valor = fibonacci_sequencia[-1] + fibonacci_sequencia[-2]
        fibonacci_sequencia.append(valor)

    print(f"Sequência de Fibonacci até o {numero_termos}º termo:")
    for i, valor_gerado in enumerate(fibonacci_sequencia):
        print(f"Termo {i+1}: {valor_gerado}")


def main():
    """
    Função principal que chama a função calcula_fibonacci.

    Returns:
        None
    """
    calcula_fibonacci()


main()
