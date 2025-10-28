"""
Calculadora de dígitos verificadores de CPF.

Este script solicita os 9 primeiros dígitos do CPF ao usuário,
calcula os dois dígitos verificadores e exibe o CPF completo formatado.

Exemplo:
    Entrada: 123456789
    Saída: CPF formatado: 123.456.789-09
"""

# Constantes
MULTIPLICADORES_DV1 = list(range(10, 1, -1))
MULTIPLICADORES_DV2 = list(range(11, 1, -1))


def solicitar_digitos_cpf():
    """
    Solicita os 9 primeiros dígitos do CPF ao usuário.

    Returns:
        list: Lista com 9 inteiros representando os dígitos do CPF.
    """
    while True:
        entrada = input(
            "Digite os 9 primeiros dígitos do CPF (somente números): "
        ).strip()
        if validar_digitos_cpf(entrada):
            return [int(d) for d in entrada]
        print("Entrada inválida. Certifique-se de digitar exatamente 9 números.")


def validar_digitos_cpf(entrada):
    """
    Valida se a entrada contém exatamente 9 números.

    Args:
        entrada (str): Entrada do usuário.

    Returns:
        bool: True se a entrada for válida, False caso contrário.
    """
    return entrada.isdigit() and len(entrada) == 9


def calcular_dv(cpf, multiplicadores):
    """
    Calcula um dígito verificador do CPF.

    Args:
        cpf (list): Lista de inteiros com os dígitos do CPF.
        multiplicadores (list): Lista de inteiros com os multiplicadores.

    Returns:
        int: Dígito verificador calculado.
    """
    soma = sum(d * m for d, m in zip(cpf, multiplicadores))
    resto = soma % 11
    return 0 if (11 - resto) > 9 else (11 - resto)


def formatar_cpf(cpf):
    """
    Formata o CPF no padrão XXX.XXX.XXX-XX.

    Args:
        cpf (list): Lista com os 11 dígitos do CPF.

    Returns:
        str: CPF formatado.
    """
    return f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"


def exibir_resultado(cpf, dv1, dv2):
    """
    Exibe os cálculos em formato de tabela.

    Args:
        cpf (list): Lista com os 9 primeiros dígitos do CPF.
        dv1 (int): Primeiro dígito verificador.
        dv2 (int): Segundo dígito verificador.

    Returns:
        None
    """
    cpf_completo = cpf + [dv1, dv2]
    print(f"CPF formatado: {formatar_cpf(cpf_completo)}")


def main():
    """Executa o fluxo principal do programa."""
    try:
        cpf = solicitar_digitos_cpf()
        dv1 = calcular_dv(cpf, MULTIPLICADORES_DV1)
        dv2 = calcular_dv(cpf + [dv1], MULTIPLICADORES_DV2)
        exibir_resultado(cpf, dv1, dv2)
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")


if __name__ == "__main__":
    main()
