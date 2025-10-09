"""Módulo para cálculo de fatoriais de múltiplos números inteiros não-negativos."""

from math import factorial


def input_controlado(mensagem, condicao, mensagem_erro):
    """Solicita um número inteiro e valida com base em uma condição.

    Args:
        mensagem: Texto exibido ao solicitar a entrada.
        condicao: Função que recebe o número e retorna True se válido.
        mensagem_erro: Texto exibido quando a entrada não atende à condição.

    Returns:
        Um número inteiro que satisfaz a condição fornecida.
    """
    while True:
        try:
            valor = int(input(mensagem))
            if condicao(valor):
                return valor
            print(mensagem_erro)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_numero(ordem):
    """Solicita ao usuário um número inteiro não-negativo.

    Args:
        ordem: Posição ordinal do número na sequência.

    Returns:
        Um número inteiro maior ou igual a zero informado pelo usuário.
    """
    return input_controlado(
        mensagem=f"Informe o {ordem}º número: ",
        condicao=lambda x: x >= 0,
        mensagem_erro="Erro: o número deve ser um inteiro não-negativo.",
    )


def ler_quantidade_numeros():
    """Solicita ao usuário a quantidade de números a serem processados.

    Returns:
        Um número inteiro maior que zero representando a quantidade de entradas.
    """

    return input_controlado(
        mensagem="Quantos números deseja calcular o fatorial? ",
        condicao=lambda x: x > 0,
        mensagem_erro="Erro: a quantidade deve ser maior que zero.",
    )


def calcular_fatoriais(lista_numeros):
    """Calcula o fatorial de cada número em uma lista.

    Args:
        lista_numeros: Lista contendo números inteiros não-negativos.

    Returns:
        Uma lista com os resultados dos fatoriais correspondentes.
    """

    return [factorial(n) for n in lista_numeros]


def exibir_resultados(numeros, fatoriais):
    """Exibe os resultados dos cálculos de fatorial no console.

    Args:
        numeros: Lista de números originais.
        fatoriais: Lista de resultados de fatorial correspondentes.
    """

    print("\n📊 Resultados:")
    for numero, fatorial in zip(numeros, fatoriais):
        print(f"Fatorial de {numero} = {fatorial}")


def main():
    """Executa o fluxo principal do programa de cálculo de fatoriais."""

    print("📌 Cálculo de Fatoriais")
    quantidade = ler_quantidade_numeros()
    numeros = [ler_numero(i + 1) for i in range(quantidade)]
    resultados = calcular_fatoriais(numeros)
    exibir_resultados(numeros, resultados)


if __name__ == "__main__":
    main()
