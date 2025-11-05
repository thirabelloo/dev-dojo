"""
Calculadora da Lei de Ohm — versão procedural.

Este módulo permite calcular tensão, corrente, resistência e potência elétrica
com base na Lei de Ohm, utilizando funções simples e interativas via terminal.
"""

SAIR = "5"


def calcular_tensao(resistencia, corrente):
    """
    Calcula a tensão elétrica (V) com base na resistência (Ω) e corrente (A).

    Args:
        resistencia (float): Valor da resistência em ohms (Ω).
        corrente (float): Valor da corrente em amperes (A).

    Returns:
        float: Tensão elétrica em volts (V).
    """
    return resistencia * corrente


def calcular_resistencia(tensao, corrente):
    """
    Calcula a resistência elétrica (Ω) com base na tensão (V) e corrente (A).

    Args:
        tensao (float): Valor da tensão em volts (V).
        corrente (float): Valor da corrente em amperes (A).

    Returns:
        float: Resistência elétrica em ohms (Ω).

    Raises:
        ValueError: Se a corrente for zero.
    """
    if corrente == 0:
        raise ValueError("A corrente não pode ser zero. Tente novamente.")
    return tensao / corrente


def calcular_corrente(tensao, resistencia):
    """
    Calcula a corrente elétrica (A) com base na tensão (V) e resistência (Ω).

    Args:
        tensao (float): Valor da tensão em volts (V).
        resistencia (float): Valor da resistência em ohms (Ω).

    Returns:
        float: Corrente elétrica em amperes (A).

    Raises:
        ValueError: Se a resistência for zero.
    """
    if resistencia == 0:
        raise ValueError("A resistência não pode ser zero. Tente novamente")
    return tensao / resistencia


def calcular_potencia(tensao, corrente):
    """
    Calcula a potência elétrica (W) com base na tensão (V) e corrente (A).

    Args:
        tensao (float): Valor da tensão em volts (V).
        corrente (float): Valor da corrente em amperes (A).

    Returns:
        float: Potência elétrica em watts (W).
    """
    return tensao * corrente


# Operações disponíveis
OPERACOES = {
    "1": {
        "nome": "Calcular Tensão Elétrica",
        "simbolo": "V",
        "funcao": calcular_tensao,
        "parametros": [
            "Digite o valor da resistência (Ω): ",
            "Digite o valor da corrente (A): ",
        ],
    },
    "2": {
        "nome": "Calcular Resistência Elétrica",
        "simbolo": "Ω",
        "funcao": calcular_resistencia,
        "parametros": [
            "Digite o valor da tensão (V): ",
            "Digite o valor da corrente (A): ",
        ],
    },
    "3": {
        "nome": "Calcular Corrente Elétrica",
        "simbolo": "A",
        "funcao": calcular_corrente,
        "parametros": [
            "Digite o valor da tensão (V): ",
            "Digite o valor da resistência (Ω): ",
        ],
    },
    "4": {
        "nome": "Calcular Potência Elétrica",
        "simbolo": "W",
        "funcao": calcular_potencia,
        "parametros": [
            "Digite o valor da tensão (V): ",
            "Digite o valor da corrente (A): ",
        ],
    },
    SAIR: {
        "nome": "Sair",
        "simbolo": "",
        "funcao": None,
        "parametros": [],
    },
}


def coletar_valor(mensagem):
    """
    Solicita ao usuário um valor numérico com base em uma mensagem.

    Args:
        mensagem (str): Mensagem a ser exibida ao usuário.

    Returns:
        float: Valor numérico fornecido pelo usuário.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido. Tente novamente.")


def exibir_menu():
    """
    Exibe o menu de operações e solicita ao usuário uma escolha.

    Returns:
        str: Código da operação escolhida pelo usuário.
    """
    print("\nMenu das Operações:")
    for codigo, dado in OPERACOES.items():
        print(f" {codigo} -> {dado['nome']}")

    while True:
        escolha = input("Escolha a operação: ").strip()
        if escolha in OPERACOES:
            return escolha
        print("Operação inválida. Escolha uma operação válida.")


def executar_operacao(codigo):
    """
    Executa a operação escolhida pelo usuário.

    Args:
        codigo (str): Código da operação escolhida.
    """
    operacao = OPERACOES[codigo]
    try:
        valores = [coletar_valor(msg) for msg in operacao["parametros"]]
        resultado = operacao["funcao"](*valores)
        print(f"\n{operacao['nome']}: {resultado:.2f} {operacao['simbolo']}")
    except ValueError as e:
        print(f"\nErro: {e}. Verifique os valores e tente novamente.")


def main():
    """
    Função principal que executa o ciclo da calculadora da Lei de Ohm.
    """
    print("🔢 Bem-vindo à Calculadora da Lei de Ohm!")
    try:
        while True:
            codigo = exibir_menu()
            if codigo == SAIR:
                print("Encerrando. Até a próxima!")
                break
            executar_operacao(codigo)
    except KeyboardInterrupt:
        print("\nInterrupção detectada. Finalizando com segurança.")


if __name__ == "__main__":
    main()
