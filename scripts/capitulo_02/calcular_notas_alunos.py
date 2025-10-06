"""
Calculadora de Média Escolar

Este script permite ao usuário informar notas de bimestres e calcula a média final,
exibindo a situação do aluno com base na tabela de aprovação.
"""


def validar_nota(valor):
    """
    Verifica se a nota está entre 0 e 100.

    Parameters:
        valor (float): Nota informada.

    Returns:
        bool: True se a nota for válida, False caso contrário.
    """

    return 0 <= valor <= 100


def calcular_media(notas):
    """
    Calcula a média aritmética das notas.

    Parameters:
        notas (list[float]): Lista de notas válidas.

    Returns:
        float: Média final.
    """

    return sum(notas) / len(notas)


def avaliar_situacao(media):
    """
    Avalia a situação do aluno com base na média.

    Parameters:
        media (float): Média final calculada.

    Returns:
        str: 'REPROVADO', 'RECUPERAÇÃO' ou 'APROVADO'.
    """

    if media < 50:
        return "REPROVADO"

    if media == 50:
        return "RECUPERAÇÃO"

    return "APROVADO"


def solicitar_nota(bimestre):
    """
    Solicita ao usuário a nota de um bimestre específico.

    Parameters:
        bimestre (int): Número do bimestre (1, 2, 3...).

    Returns:
        float: Nota válida entre 0 e 100.
    """

    while True:
        try:
            nota = float(input(f"Digite a nota do {bimestre}º bimestre: "))
            if validar_nota(nota):
                return nota
            print("A nota deve estar entre 0 e 100. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite uma nota válida.")


def solicitar_quantidade_notas():
    """
    Solicita ao usuário a quantidade de notas a serem informadas.

    Returns:
        int: Quantidade válida (maior que zero).
    """

    while True:
        try:
            quantidade = int(input("Digite a quantidade de notas: "))
            if quantidade > 0:
                return quantidade
            print("A quantidade de notas deve ser maior que zero")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def main():
    """
    Função principal que executa o fluxo completo:
    - Solicita quantidade de notas
    - Coleta as notas
    - Calcula a média
    - Exibe a situação do aluno
    """
    quantidade = solicitar_quantidade_notas()
    notas = [solicitar_nota(i + 1) for i in range(quantidade)]
    media = calcular_media(notas)
    status = avaliar_situacao(media)
    print(f"\n📊 Média final: {media:.2f}")
    print(f"📌 Situação do aluno: {status}")


if __name__ == "__main__":
    main()
