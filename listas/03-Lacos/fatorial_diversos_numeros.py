"""Script que calcula fatorial de N números inteiros"""

import math


def calcula_fatorial(numero):
    """
    Calcula o fatorial de um número.

    Parâmetros:
        numero (int): Número para o qual calcular o fatorial.

    Retorna:
        int: Fatorial do número. Lança: ValueError: Se o número for negativo.
    """
    if numero < 0:
        raise ValueError("As entradas devem ser números inteiros positivos.")
    return math.factorial(numero)


def coleta_numeros(quantidade_numero):
    """Coleta uma quantidade especificada de números inteiros do usuário.

    Parâmetros:
        quantidade (int): Quantidade de números a serem coletados.

    Retorna:
        list: Lista de números inteiros coletados.
    """
    lista_numeros = []
    for i in range(1, quantidade_numero + 1):
        while True:
            try:
                entrada = int(input(f"Digite o {i}º número: "))
                if entrada < 0:
                    print("Erro: Insira um número inteiro não negativo.")
                    continue
                lista_numeros.append(entrada)
                break
            except ValueError:
                print("Erro: Insira um número inteiro válido.")
    return sorted(lista_numeros)


def pergunta_quantidade():
    """
    Pergunta ao usuário quantos números ele deseja inserir.

    Retorna:
        int: Quantidade de números a serem inseridos.
    """
    while True:
        try:
            quantidade = int(input("Quantos números você deseja inserir? "))
            if quantidade > 0:
                return quantidade
            print("A quantidade deve ser um número inteiro positivo.")
        except ValueError:
            print("Erro: Insira um número inteiro válido.")


def imprimir_fatoriais(numeros):
    """
    Imprime o fatorial de uma lista de números.

    Parâmetros:
        numeros (list): Lista de números inteiros.
    """
    for numero in numeros:
        try:
            if numero < 0:
                raise ValueError("Número deve ser não negativo.")
            fatorial_calculada = calcula_fatorial(numero)
            print(f"O fatorial de {numero} é {fatorial_calculada}")
        except ValueError as error:
            print(f"Erro ao calcular o fatorial de {numero}: {error}")


def main():
    """
    Função principal que coordena a execução do programa.
    """
    quantidade_numeros = pergunta_quantidade()
    numeros_coletados = coleta_numeros(quantidade_numeros)
    imprimir_fatoriais(numeros_coletados)


main()
