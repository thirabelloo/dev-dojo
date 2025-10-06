"""
Calculadora de IMC (Índice de Massa Corporal).

Solicita peso e altura do paciente, calcula o IMC e classifica
de acordo com os critérios da Organização Mundial da Saúde.
"""


def solicitar_valor(mensagem, valor_minimo, valor_maximo):
    """
    Solicita ao usuário um valor numérico dentro de um intervalo permitido.

    Args:
        mensagem (str): Texto de orientação para o usuário.
        valor_minimo (float): Valor mínimo permitido.
        valor_maximo (float): Valor máximo permitido.

    Returns:
        float: Valor numérico validado.
    """

    while True:
        try:
            valor = float(input(mensagem))
            if valor_minimo <= valor <= valor_maximo:
                return valor
            print(f"Valor fora do intervalo permitido ({valor_minimo}–{valor_maximo}).")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def calcular_imc(peso, altura):
    """
    Calcula o IMC com base no peso e altura.

    Args:
        peso (float): Peso em quilogramas.
        altura (float): Altura em metros.

    Returns:
        float: Valor do IMC.
    """

    return peso / altura**2


def classificar_imc(imc):
    """
    Classifica o IMC de acordo com os critérios da OMS.

    Args:
        imc (float): Valor do IMC.

    Returns:
        str: Classificação correspondente.
    """
    classificacoes = {
        "🟣 Desnutrição Grau V": (0, 9.9),
        "🔴 Desnutrição Grau IV": (10, 12.9),
        "🔴 Desnutrição Grau III": (13, 15.9),
        "🟠 Desnutrição Grau II": (16, 16.9),
        "🟡 Desnutrição Grau I": (17, 18.4),
        "✅ Normal": (18.5, 24.9),
        "⚠️ Pré-obesidade": (25, 29.9),
        "⚠️ Obesidade Grau I": (30, 34.5),
        "⚠️ Obesidade Grau II": (35, 39.9),
        "🚨 Obesidade Grau III": (40, float("inf")),
    }

    for classificao, (min_valor, max_valor) in classificacoes.items():
        if min_valor <= imc <= max_valor:
            return classificao
    return "IMC fora da faixa conhecida."


def main():
    """
    Função principal que coordena a execução da calculadora de IMC.
    """
    print("📊 Calculadora de IMC")
    peso = solicitar_valor("Digite o seu peso (kg): ", 1, 200)
    altura = solicitar_valor("Digite a sua altura (m): ", 0.5, 2.5)
    imc = calcular_imc(peso=peso, altura=altura)
    classificacao = classificar_imc(imc=imc)
    print(f"\n🧮 Seu IMC é: {imc:.2f}")
    print(f"📋 Classificação: {classificacao}")


if __name__ == "__main__":
    main()
