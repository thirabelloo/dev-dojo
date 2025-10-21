"""
Este módulo implementa uma calculadora de linha de comando que permite ao usuário
realizar operações matemáticas básicas: adição, subtração, multiplicação e divisão.

O usuário escolhe a operação, insere dois números e recebe o resultado.
A calculadora continua em execução até que o usuário escolha a opção de sair.
"""

# Constantes
SAIR = "0"

# Mapeamento de operadores para funções matemáticas
OPERACOES = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else None,
}

# Nomes das operações
NOMES_OPERACOES = {
    "+": "Adição",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    SAIR: "Sair",
}


def nome_operacao(simbolo):
    """
    Retorna o nome da operação correspondente ao símbolo fornecido.

    Args:
        simbolo (str): Símbolo da operação matemática.

    Returns:
        str: Nome da operação ou 'Desconhecida' se o símbolo não for reconhecido.
    """
    return NOMES_OPERACOES.get(simbolo, "Desconhecida")


def exibir_menu():
    """
    Exibe o menu de operações disponíveis e solicita a escolha do usuário.

    Returns:
        str: Símbolo da operação escolhida pelo usuário.
    """
    print("\nOperações disponíveis:")
    for simbolo, nome in NOMES_OPERACOES.items():
        print(f" {simbolo} -> {nome}")

    while True:
        escolha = input("Escolha a operação desejada: ").strip()
        if escolha in NOMES_OPERACOES:
            return escolha
        print("Operação inválida. Escolha uma operação válida.")


def obter_numero(posicao):
    """
    Solicita ao usuário um número decimal, validando a entrada.

    Args:
        posicao (str): Indicação da posição do número ('primeiro', 'segundo').

    Returns:
        float: Número decimal informado pelo usuário.
    """

    while True:
        try:
            return float(input(f"Digite o {posicao} número: "))
        except ValueError:
            print("Erro: Digite um número válido.")


def calcular(operador, a, b):
    """
    Realiza o cálculo com base na operação escolhida e nos valores fornecidos.

    Args:
        operador (str): Símbolo da operação matemática.
        a (float): Primeiro número.
        b (float): Segundo número.

    Returns:
        str: Resultado formatado ou mensagem de erro.
    """

    resultado = OPERACOES[operador](a, b)
    if resultado is None:
        return "Erro: divisão por zero não é permitida."
    return f"Resultado: {a} {operador} {b} = {resultado}"


def main():
    """
    Função principal que coordena a execução da calculadora.
    """
    print("🧮 Bem-vindo à Calculadora Interativa!")
    while True:
        operacao = exibir_menu()
        if operacao == SAIR:
            print("Encerrando a calculadora. Até mais!")
            break
        a = obter_numero("primeiro")
        b = obter_numero("segundo")
        resultado = calcular(operacao, a, b)
        print(f"\n{resultado}")


if __name__ == "__main__":
    main()
