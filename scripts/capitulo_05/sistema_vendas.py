"""Sistema de vendas com operações de cálculo e histórico de transações."""

from collections import deque

# Constantes
LIMITE_VENDAS = 5
COMISSAO_VENDEDOR = 0.25
IMPOSTOS_E_TAXAS = 0.65
JUROS_PARCELAMENTO = 0.02
DESCONTO_MAXIMO = 15
DESCONTO_MINIMO = 0
PARCELAS_MINIMAS = 3
PARCELAS_MAXIMAS = 36
SAIR = "6"
OPCAO_VISUALIZAR_VENDAS = "5"


def coletar_dado(mensagem, tipo_dado, mensagem_erro):
    """
    Solicita um dado ao usuário, converte para o tipo especificado e trata erros de entrada.

    Args:
        mensagem (str): Texto exibido ao solicitar o dado.
        tipo_dado (type): Tipo ao qual o dado deve ser convertido.
        mensagem_erro (str): Mensagem exibida em caso de erro de conversão.

    Returns:
        tipo_dado: Valor convertido, se válido.
    """
    while True:
        try:
            return tipo_dado(input(mensagem))
        except ValueError:
            print(f"Erro: {mensagem_erro}")


def validar_valor_positivo(valor, nome_campo):
    """
    Valida se o valor informado é positivo.

    Args:
        valor (float): Valor a ser validado.
        nome_campo (str): Nome do campo para exibir na mensagem de erro.

    Returns:
        bool: True se válido, False se inválido.
    """
    if valor <= 0:
        print(f"Erro: O valor {nome_campo} deve ser maior que zero.")
        return False
    return True


def executar_operacao(funcao, entradas, mensagem_final=None, historico=None):
    """
    Executa uma função com base em entradas coletadas e exibe o resultado formatado.

    Args:
        funcao (callable): Função a ser executada.
        entradas (list): Lista de dicionários com instruções de entrada.
        mensagem_final (str, optional): Texto formatado para exibir o resultado.
        historico (deque, optional): Histórico para armazenar o resultado.
    """

    valores = [
        coletar_dado(dado["mensagem"], dado["tipo"], dado["erro"]) for dado in entradas
    ]
    resultado = funcao(*valores)
    if resultado is not None:
        print(mensagem_final.format(resultado=resultado))
        if historico is not None:
            historico.append(resultado)


def realizar_venda(valor_produto):
    """
    Calcula o valor total da venda com comissão e impostos.

    Args:
        valor_produto (float): Valor base do produto.

    Returns:
        float or None: Valor total da venda, ou None se o valor for inválido.
    """
    if not validar_valor_positivo(valor_produto, "do produto"):
        return None
    comissao = valor_produto * COMISSAO_VENDEDOR
    imposto = valor_produto * IMPOSTOS_E_TAXAS
    return valor_produto + comissao + imposto


def calcular_pagamento_a_vista(valor_pagamento, desconto):
    """
    Aplica desconto ao pagamento à vista, validando os limites permitidos.

    Args:
        valor_pagamento (float): Valor original do pagamento.
        desconto (float): Percentual de desconto.

    Returns:
        float or None: Valor com desconto, ou None se inválido.
    """
    if not validar_valor_positivo(valor_pagamento, "do pagamento"):
        return None

    if not DESCONTO_MINIMO <= desconto <= DESCONTO_MAXIMO:
        print(
            f"Erro: O desconto deve estar entre {DESCONTO_MINIMO}% e {DESCONTO_MAXIMO}%."
        )
        return None
    return round(valor_pagamento * (1 - desconto / 100), 2)


def calcular_pagamento_parcelado(valor_pagamento, numero_parcelas):
    """
    Calcula o valor total do pagamento parcelado com juros por parcela.

    Args:
        valor_pagamento (float): Valor original do pagamento.
        numero_parcelas (int): Quantidade de parcelas.

    Returns:
        float or None: Valor com juros, ou None se inválido.
    """
    if not validar_valor_positivo(valor_pagamento, "do pagamento"):
        return None
    if not PARCELAS_MINIMAS <= numero_parcelas <= PARCELAS_MAXIMAS:
        print(
            f"Erro: O número de parcelas deve estar entre {PARCELAS_MINIMAS} e {PARCELAS_MAXIMAS}."
        )
        return None
    acrescimo = valor_pagamento * JUROS_PARCELAMENTO * numero_parcelas
    return round(valor_pagamento + acrescimo, 2)


def calcular_prestacao_em_atraso(valor_prestacao, taxa_juros, dias_atraso):
    """
    Calcula o valor de uma prestação em atraso com base na taxa e dias.

    Args:
        valor_prestacao (float): Valor original da prestação.
        taxa_juros (float): Taxa de juros aplicada.
        dias_atraso (int): Número de dias em atraso.

    Returns:
        float: Valor final da prestação com juros.
    """
    if not validar_valor_positivo(valor_prestacao, "da prestação"):
        return None
    return valor_prestacao + (valor_prestacao * (taxa_juros / 100) * dias_atraso)


def exibir_ultimas_vendas(historico):
    """
    Exibe as últimas vendas realizadas e o total acumulado.

    Args:
        historico (deque): Lista com os valores das últimas vendas.
    """
    print("\nÚltimas Vendas Realizadas:")
    if not historico:
        print("Nenhuma venda registrada até o momento.")
    else:
        for i, venda in enumerate(historico, start=1):
            print(f"{i}. Valor da Venda: R$ {venda:,.2f}")
        print("-" * 30)
        print(f"Total de Vendas Registradas: {len(historico)}\n")
        print(f"Valor Total das Vendas: R$ {sum(historico)}\n")


def operacoes():
    """
    Define o conjunto de operações disponíveis no sistema.

    Returns:
        dict: Dicionário com as operações e suas configurações.
    """
    return {
        "1": {
            "descricao": "Realizar Venda",
            "funcao": realizar_venda,
            "entradas": [
                {
                    "mensagem": "Valor do produto: R$ ",
                    "tipo": float,
                    "erro": "Entrada inválida. Informe o valor do produto usando números decimais (ex: 199.90).",
                }
            ],
            "mensagem_final": "Venda realizada! Total: R$ {resultado:.2f}",
            "usa_historico": True,
        },
        "2": {
            "descricao": "Pagamento à Vista com Desconto",
            "funcao": calcular_pagamento_a_vista,
            "entradas": [
                {
                    "mensagem": "Valor do pagamento: R$ ",
                    "tipo": float,
                    "erro": "Entrada inválida. Informe o valor do pagamento usando números decimais.",
                },
                {
                    "mensagem": "Desconto (%): ",
                    "tipo": float,
                    "erro": "Entrada inválida. Informe o percentual de desconto entre 0 e 15 (ex: 10.5).",
                },
            ],
            "mensagem_final": "Valor com desconto: R$ {resultado:.2f}",
        },
        "3": {
            "descricao": "Pagamento Parcelado com Juros",
            "funcao": calcular_pagamento_parcelado,
            "entradas": [
                {
                    "mensagem": "Valor do pagamento: R$ ",
                    "tipo": float,
                    "erro": "Entrada inválida. Informe o valor do pagamento usando números decimais.",
                },
                {
                    "mensagem": "Número de parcelas (3 a 36): ",
                    "tipo": int,
                    "erro": "Entrada inválida. Informe um número inteiro entre 3 e 36 para as parcelas.",
                },
            ],
            "mensagem_final": "Valor parcelado: R$ {resultado:.2f}",
        },
        "4": {
            "descricao": "Prestação em Atraso",
            "funcao": calcular_prestacao_em_atraso,
            "entradas": [
                {
                    "mensagem": "Valor da prestação: R$ ",
                    "tipo": float,
                    "erro": "Entrada inválida. Informe o valor da prestação usando números decimais.",
                },
                {
                    "mensagem": "Taxa de juros (%): ",
                    "tipo": float,
                    "erro": "Entrada inválida. Informe a taxa de juros como número decimal (ex: 2.5).",
                },
                {
                    "mensagem": "Dias de atraso: ",
                    "tipo": int,
                    "erro": "Entrada inválida. Informe o número de dias de atraso como um valor inteiro.",
                },
            ],
            "mensagem_final": "Valor com atraso: R$ {resultado:.2f}",
        },
        "5": {
            "descricao": "Visualizar Últimas Vendas",
            "funcao": exibir_ultimas_vendas,
        },
        "6": {
            "descricao": "Sair do Sistema",
            "funcao": None,
        },
    }


def menu_principal(historico, operacao):
    """
    Exibe o menu principal e gerencia a execução das operações.

    Args:
        historico (deque): Histórico de vendas.
        operacao (dict): Operações disponíveis.
    """

    while True:
        print("\nBem-vindo(a) ao sistema de vendas Express🐊!\n")
        for chave, op in operacao.items():
            print(f"{chave}. {op['descricao']}")

        escolha = input("\nEscolha uma opção: ")
        operacao = operacao.get(escolha)

        if not operacao:
            print("Opção inválida. Tente novamente.")
            continue

        if escolha == SAIR:
            print("Encerrando o sistema. Até logo!")
            break

        funcao = operacao["funcao"]

        if escolha == OPCAO_VISUALIZAR_VENDAS:
            funcao(historico)
        else:
            executar_operacao(
                funcao=funcao,
                entradas=operacao["entradas"],
                mensagem_final=operacao["mensagem_final"],
                historico=historico if operacao.get("usa_historico") else None,
            )


def main():
    """
    Ponto de entrada do sistema de vendas Express🐊.
    Inicializa o histórico e inicia o menu principal.
    """
    try:
        historico_vendas = deque(maxlen=LIMITE_VENDAS)
        operacao = operacoes()
        menu_principal(historico_vendas, operacao)
    except KeyboardInterrupt:
        print("\nEncerrando o sistema. Até logo!")


if __name__ == "__main__":
    main()
