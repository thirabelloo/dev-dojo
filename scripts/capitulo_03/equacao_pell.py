"""
Módulo de cálculo da raiz quadrada utilizando a Equação de Pell.

Este módulo implementa funções para calcular a parte inteira da raiz quadrada
de um número inteiro positivo utilizando subtrações sucessivas de números ímpares consecutivos.
Também permite calcular uma aproximação da raiz quadrada com casas decimais.
"""


def coletar_numero(texto):
    """
    Solicita ao usuário um número inteiro positivo.

    Args:
        texto (str): Mensagem exibida ao usuário.

    Returns:
        int: Número inteiro positivo fornecido pelo usuário.
    """
    while True:
        try:
            numero = int(input(texto))
            if numero >= 0:
                return numero
            print("Erro: o número deve ser não-negativo.")
        except ValueError:
            print("Entrada inválida: digite um número inteiro.")


def raiz_pell_inteira(numero):
    """
    Calcula a parte inteira da raiz quadrada de um número usando a Equação de Pell.

    Args:
        numero (int): Número inteiro positivo.

    Returns:
        int: Parte inteira da raiz quadrada do número.
    """
    contador = 0
    impar = 1

    while numero >= impar:
        numero -= impar
        impar += 2
        contador += 1
    return contador


def raiz_pell_decimal(numero, casas=5):
    """
    Calcula a raiz quadrada aproximada de um número com casas decimais.

    Args:
        numero (int): Número inteiro positivo.
        casas (int, optional): Número de casas decimais desejadas. Default é 5.

    Returns:
        float: Raiz quadrada aproximada com o número especificado de casas decimais.
    """
    parte_inteira = raiz_pell_inteira(numero)
    resultado = parte_inteira
    incremento = 0.1

    for _ in range(casas):
        while (resultado + incremento) ** 2 <= numero:
            resultado += incremento
        incremento /= 10

    return round(resultado, casas)


def main():
    """
    Função principal que executa o cálculo da raiz quadrada.

    Solicita ao usuário um número inteiro positivo, calcula a parte inteira
    e a raiz aproximada com casas decimais, e exibe os resultados.
    """
    print("🔢 Cálculo da raiz quadrada pela Equação de Pell")

    numero = coletar_numero("Digite um número inteiro positivo: ")
    raiz_inteira = raiz_pell_inteira(numero)
    raiz_aproximada = raiz_pell_decimal(numero)

    print(f"\n✅ Parte inteira da raiz de {numero}: {raiz_inteira}")
    print(f"📐 Raiz aproximada com decimais: {raiz_aproximada}")


if __name__ == "__main__":
    main()
