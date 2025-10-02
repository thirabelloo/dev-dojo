"""
Calculadora Elétrica - Lei de Ohm

Este módulo permite calcular resistência, tensão, corrente e potência elétrica
com base nas fórmulas da Lei de Ohm.
"""


def coletar_valores(entradas):
    """
    Solicita ao usuário os valores necessários para o cálculo.

    Parameters:
        entradas (list): Lista de tuplas contendo a chave e a mensagem de entrada.

    Returns:
        dict: Dicionário com os valores convertidos para float.
    """

    valores = {}
    for chave, mensagem in entradas:
        while True:
            try:
                valores[chave] = float(input(mensagem))
                break
            except ValueError:
                print("Entrada inválida. Digite um valor numérico.")
    return valores


def calcular_resistencia(tensao, corrente):
    """
    Calcula a resistência elétrica usando a fórmula R = U / I.

    Parameters:
        tensao (float): Tensão elétrica em Volts.
        corrente (float): Corrente elétrica em Amperes.

    Returns:
        float: Resistência elétrica em Ohms.
    """

    if corrente == 0:
        raise ValueError("A Corrente não pode ser zero. Tente novamente")
    return tensao / corrente


def calcular_tensao(resistencia, corrente):
    """
    Calcula a tensão elétrica usando a fórmula U = R * I.

    Parameters:
        resistencia (float): Resistência elétrica em Ohms.
        corrente (float): Corrente elétrica em Amperes.

    Returns:
        float: Tensão elétrica em Volts.
    """

    return resistencia * corrente


def calcular_corrente(tensao, resistencia):
    """
    Calcula a corrente elétrica usando a fórmula I = U / R.

    Parameters:
        tensao (float): Tensão elétrica em Volts.
        resistencia (float): Resistência elétrica em Ohms.

    Returns:
        float: Corrente elétrica em Amperes.
    """

    if resistencia == 0:
        raise ValueError("A Resistência não pode ser zero. Tente novamente")
    return tensao / resistencia


def calcular_potencia(tensao, corrente):
    """
    Calcula a potência elétrica usando a fórmula P = U * I.

    Parameters:
        tensao (float): Tensão elétrica em Volts.
        corrente (float): Corrente elétrica em Amperes.

    Returns:
        float: Potência elétrica em Watts.
    """

    return tensao * corrente


OPERACOES = {
    "1": {
        "nome": "Resistência",
        "unidade": "Ω",
        "funcao": calcular_resistencia,
        "entradas": [
            ("tensao", "Digite a tensão (Volts): "),
            ("corrente", "Digite a corrente (Amperes): "),
        ],
    },
    "2": {
        "nome": "Tensão",
        "unidade": "V",
        "funcao": calcular_tensao,
        "entradas": [
            ("resistencia", "Digite a resistência (Ohms): "),
            ("corrente", "Digite a corrente (Amperes): "),
        ],
    },
    "3": {
        "nome": "Corrente",
        "unidade": "A",
        "funcao": calcular_corrente,
        "entradas": [
            ("tensao", "Digite a tensão (Volts): "),
            ("resistencia", "Digite a resistência (Ohms): "),
        ],
    },
    "4": {
        "nome": "Potência",
        "unidade": "W",
        "funcao": calcular_potencia,
        "entradas": [
            ("tensao", "Digite a tensão (Volts): "),
            ("corrente", "Digite a corrente (Amperes): "),
        ],
    },
}


def menu():
    """
    Exibe o menu principal com as opções de cálculo disponíveis.
    """

    print("\n********** 📐 Calculadora Elétrica - Lei de Ohm **********")
    for codigo, dados in OPERACOES.items():
        print(f"{codigo}. Calcular {dados["nome"]}")
    print("0. Sair")


def executar_operacao(codigo):
    """
    Executa a operação selecionada pelo usuário com base no código fornecido.

    Parameters:
        codigo (str): Código da operação a ser executada.
    """

    dados = OPERACOES[codigo]
    valores = coletar_valores(dados["entradas"])
    resultado = dados["funcao"](**valores)
    print(f"{dados['nome']}: {resultado:.2f} {dados['unidade']}")


def main():
    """
    Função principal que controla o fluxo da calculadora elétrica.
    """

    while True:
        menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "0":
            print("👋 Encerrando a calculadora. Até mais!")
            break

        if opcao in OPERACOES:
            try:
                executar_operacao(opcao)
            except ValueError as erro:
                print(f"Erro: {erro}")
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
