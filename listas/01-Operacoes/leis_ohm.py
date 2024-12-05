""" Este Script o fornece funções para realizar cálculos usando a Lei de Ohm. """


def exibir_menu():
    """Exibe o menu de operações disponíveis para o usuário."""
    menu_texto = """
    ********** Operacoes com a Lei de Ohm **********\n
    Selecione o numero da operacao desejada:
    1 - Calcular a Resistencia (R)
    2 - Calcular a Tensao (U)
    3 - Calcular a Corrente (I)
    4 - Calcular a Potencia (P)
    5 - Sair
    """
    print(menu_texto)


def entrada_usuario(mensagem):
    """
    Obtém um número do usuário e lida com entradas inválidas.

    Parâmetros:
    mensagem (str): A mensagem a ser exibida ao usuário ao solicitar o número.

    Levanta:
    ValueError: Se o usuário não inserir um número válido.

    Retorna:
    float: O número válido inserido pelo usuário.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("\nEntrada invalida. Por favor, insira um numero valido")


def calcular_resistencia(tensao, corrente):
    """
    Calcula a resistência com base na tensão e corrente fornecidas.

    Parâmetros:
    tensao (float): O valor da tensão em volts.
    corrente (float): O valor da corrente em amperes.

    Levanta:
    ValueError: Se a corrente for zero, pois isso resultaria em divisão por zero.

    Retorna:
    str: A resistência calculada em ohms.
    """
    if corrente == 0:
        return "Não podemos dividir por zero."
    return f"{tensao / corrente:.2f} ohms"


def calcular_tensao(resistencia, corrente):
    """
    Calcula a tensão com base na resistência e corrente fornecidas.

    Parâmetros:
    resistencia (float): O valor da resistência em ohms.
    corrente (float): O valor da corrente em amperes.

    Retorna:
    str: A tensão calculada em volts.
    """
    return f"{resistencia * corrente:.2f} volts"


def calcular_corrente(tensao, resistencia):
    """
    Calcula a corrente com base na tensão e resistência fornecidas.

    Parâmetros:
    tensao (float): O valor da tensão em volts.
    resistencia (float): O valor da resistência em ohms.

    Levanta:
    ValueError: Se a resistência for zero, pois isso resultaria em divisão por zero.

    Retorna:
    str: A corrente calculada em amperes.
    """
    if resistencia == 0:
        return "Não podemos dividir por zero."
    return f"{tensao / resistencia:.2f} amperes"


def calcular_potencia(tensao, corrente):
    """
    Calcula a potência com base na tensão e corrente fornecidas.

    Parâmetros:
    tensao (float): O valor da tensão em volts.
    corrente (float): O valor da corrente em amperes.

    Retorna:
    str: A potência calculada em watts.
    """
    return f"{tensao * corrente:.2f} watts"


def realizar_operacao(operacao, tensao, corrente, resistencia):
    """
    Realiza a operação desejada de acordo com a seleção do usuário.

    Parâmetros:
    operacao (str): Operação selecionada pelo usuário.
    tensao (float): Valor da tensão fornecida.
    corrente (float): Valor da corrente fornecida.
    resistencia (float): Valor da resistência fornecida.

    Retorna:
    str: Resultado da operação ou mensagem de erro.
    """
    operacoes = {
        "1": calcular_resistencia,
        "2": calcular_tensao,
        "3": calcular_corrente,
        "4": calcular_potencia,
    }
    if operacao in operacoes:
        funcao = operacoes[operacao]
        if operacao == "1":
            return funcao(tensao, corrente)
        if operacao == "2":
            return funcao(resistencia, corrente)
        if operacao == "3":
            return funcao(tensao, resistencia)
        if operacao == "4":
            return funcao(tensao, corrente)
    return "Operação inválida"


def lei_ohm():
    """
    Executa o menu de operações com a Lei de Ohm, recebendo e processando a entrada do usuário.
    """
    while True:
        exibir_menu()
        operacao = input("Digite sua opção: ")

        if operacao == "5":
            print("Saindo...")
            break

        if operacao not in {"1", "2", "3", "4"}:
            print("Opção inválida. Por favor, escolha uma das opções do menu.\n")
            continue

        tensao = corrente = resistencia = 0
        if operacao in {"1", "3", "4"}:
            tensao = entrada_usuario("Digite o valor da tensão (em volts): ")
        if operacao in {"1", "2", "4"}:
            corrente = entrada_usuario("Digite o valor da corrente (em amperes): ")
        if operacao in {"2", "3"}:
            resistencia = entrada_usuario("Digite o valor da resistência (em ohms): ")

        resultado = realizar_operacao(operacao, tensao, corrente, resistencia)
        if "Erro" in resultado or "Operação inválida" in resultado:
            print(f"\n{resultado}\n")
        else:
            print(f"\nResultado: {resultado}\n")

        if input("Deseja realizar outra operacao? (s/n): ").lower() != "s":
            print("Saindo do programa. Até a próxima!")
            break
