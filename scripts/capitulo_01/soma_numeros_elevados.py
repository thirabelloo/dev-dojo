"""
Este módulo solicita um número ao usuário, calcula seu quadrado, cubo, décima potência e exibe a soma dessas potências.
"""


def obter_numero(mensagem):
    """
    Solicita ao usuário um número maior que zero.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        float: Número informado pelo usuário.
    """
    while True:
        try:
            numero = float(input(mensagem))
            if numero > 0:
                return numero
            print("Atenção: O número precisa ser maior que zero.")
        except ValueError:
            print("Erro: Digite apenas números, sem letras ou símbolos.")


def calcular_potenciais(numero):
    """
    Calcula o quadrado, cubo, décima potência e a soma dessas potências de um número.

    Args:
        numero (float): Número para cálculo das potências.

    Returns:
        tuple: Quadrado, cubo, décima potência e soma das potências.
    """
    quadrado = numero**2
    cubo = numero**3
    decima = numero**10
    soma = quadrado + cubo + decima
    return quadrado, cubo, decima, soma


def exibir_resultados(numero, quadrado, cubo, decima, soma):
    """
    Exibe os resultados dos cálculos das potências e sua soma.

    Args:
        numero (float): Número informado pelo usuário.
        quadrado (float): Quadrado do número.
        cubo (float): Cubo do número.
        decima (float): Décima potência do número.
        soma (float): Soma das potências.
    """
    print("\n📊 Resultados:")
    print(f"Número informado: {numero}")
    print(f"Quadrado: {quadrado}")
    print(f"Cubo: {cubo}")
    print(f"Décima potência: {decima}")
    print(f"Soma das potências: {soma}\n")


def main():
    """
    Função principal que executa o cálculo das potências e exibe os resultados.
    """
    print("🔢 Cálculo de Potências")
    numero = obter_numero("Digite um número maior que zero: ")
    quadrado, cubo, decima, soma = calcular_potenciais(numero)
    exibir_resultados(numero, quadrado, cubo, decima, soma)


if __name__ == "__main__":
    main()
