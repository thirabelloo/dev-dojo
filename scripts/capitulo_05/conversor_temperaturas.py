"""Script de conversão de temperaturas entre Celsius e Fahrenheit com histórico de operações."""

from collections import deque

# Constantes
SAIR = "4"
HISTORICO_LIMITE = 5
VISUALIZAR_HISTORICO = "3"


OPERACOES = {
    "1": {
        "nome": "Converter de graus Celsius para Fahrenheit",
        "origem": "°C",
        "destino": "°F",
        "func": lambda celsius: (9 / 5 * celsius) + 32,
    },
    "2": {
        "nome": "Converter de graus Fahrenheit para Celsius",
        "origem": "°F",
        "destino": "°C",
        "func": lambda fahrenheit: ((fahrenheit - 32) * 5) / 9,
    },
    "3": {
        "nome": "Visualizar as últimas 5 operações",
        "origem": None,
        "destino": None,
        "func": None,
    },
    SAIR: {
        "nome": "Sair",
        "origem": None,
        "destino": None,
        "func": None,
    },
}


def coletar_temperatura(unidade):
    """
    Solicita ao usuário uma temperatura numérica na unidade especificada.

    Args:
        unidade (str): Unidade de temperatura ("°C" ou "°F").

    Returns:
        float: Valor da temperatura fornecido pelo usuário.
    """

    while True:
        try:
            return float(input(f"Digite a temperatura em {unidade}: ").strip())
        except ValueError:
            print("Erro: A temperatura deve ser um número.")


def exibir_menu():
    """
    Exibe o menu de opções e solicita ao usuário uma escolha válida.

    Returns:
        str: Código da operação escolhida.
    """
    print("\n🌡️  Conversor de Temperaturas — selecione uma opção abaixo:")
    for codigo, dados in OPERACOES.items():
        print(f" {codigo} -> {dados['nome']}")
    while True:
        escolha = input("Escolha a opção desejada: ").strip()
        if escolha in OPERACOES:
            return escolha
        print("Opção inválida. Tente novamente.")


def exibir_historico(historico):
    """
    Exibe o histórico das últimas conversões realizadas.

    Args:
        historico (deque): Lista limitada de conversões registradas.
    """
    print("\n📚 Histórico de conversões:")
    if not historico:
        print("Nenhuma conversão registrada até o momento.")
    else:
        for i, item in enumerate(historico, start=1):
            print(f"{i}. {item}")
        print("-" * 40)
        print(f"Total de registros: {len(historico)}")


def executar_conversao(codigo, historico):
    """
    Executa a conversão de temperatura com base na operação escolhida.

    Args:
        codigo (str): Código da operação.
        historico (deque): Lista de histórico para registrar a conversão.
    """

    operacao = OPERACOES[codigo]
    origem = operacao["origem"]
    destino = operacao["destino"]
    funcao = operacao["func"]

    valor = coletar_temperatura(origem)
    resultado = funcao(valor)
    texto = f"{valor:.2f}{origem} = {resultado:.2f}{destino}"
    print(f"\nResultado: {texto}")
    historico.append(texto)


def main():
    """
    Função principal que executa o ciclo interativo do conversor de temperaturas.
    """
    historico = deque(maxlen=HISTORICO_LIMITE)
    try:
        while True:
            codigo = exibir_menu()
            if codigo == SAIR:
                print(
                    "Encerrando... Obrigado por utilizar o conversor de temperaturas."
                )
                break
            if codigo == VISUALIZAR_HISTORICO:
                exibir_historico(historico)
            else:
                executar_conversao(codigo, historico)
    except KeyboardInterrupt:
        print("\nInterrupção detectada. Finalizando com segurança.")


if __name__ == "__main__":
    main()
