"""
Este módulo permite inverter os valores de duas variáveis informadas pelo usuário.
"""


def inverter_valores(valor_x, valor_y):
    """
    Inverte os valores entre duas variáveis.

    Args:
        valor_x: Primeiro valor.
        valor_y: Segundo valor.

    Returns:
        tuple: Uma tupla com os valores invertidos (valor_y, valor_x).
    """

    return valor_y, valor_x


def solicitar_numero(mensagem):
    """
    Solicita ao usuário um valor numérico.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        float: Valor informado pelo usuário.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def main():
    """
    Função principal que executa a troca de valores.
    """
    print("\n🔄 Troca de Valores")
    numero_x = solicitar_numero("Digite o valor de X: ")
    numero_y = solicitar_numero("Digite o valor de Y: ")

    numero_x, numero_y = inverter_valores(numero_x, numero_y)
    print(f"\nAntes da troca, X = {numero_y} e Y = {numero_x}")
    print(f"Após a troca, X = {numero_x} e Y = {numero_y}")


if __name__ == "__main__":
    main()
