"""Script que calcula as notas de N bimestres, imprime sua media e a situacao do aluno"""


def obter_notas_bimestre(bimestres):
    """
    Recebe a nota de um bimestre e garante que esteja entre 0 e 100.

    Args:
        bimestres (int): O número do bimestre (1 a N).

    Returns:
        float: A nota validada entre 0 e 100.
    """
    while True:
        try:
            nota = float(input(f"Digite a nota do {bimestres}º bimestre: "))
            if 0 <= nota <= 100:
                return nota
            return "Nota deve estar entre 0 e 100. Tente novamente."
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def calcular_media(notas):
    """
    Calcula a média das notas fornecidas.

    Args:
        notas (list of float): Lista de notas.

    Returns:
        float: A média das notas.
    """
    return sum(notas) / len(notas)


def situacao_status_alunos(media):
    """
    Determina o status do aluno baseado na média das notas.

    Args:
        media (float): A média das notas.

    Returns:
        str: O status do aluno ('REPROVADO', 'RECUPERAÇÃO' ou 'APROVADO').
    """
    if media < 50:
        return "REPROVADO"
    if media == 50:
        return "RECUPERAÇÃO"
    return "APROVADO"


def main():
    """
    Função principal que orquestra a coleta de notas, cálculo da média e exibição do status.
    """
    try:
        total_notas = int(input("Digite a quantidade de notas: "))
        if total_notas <= 0:
            raise ValueError("A quantidade de notas deve ser maior que zero")

        notas = [obter_notas_bimestre(i + 1) for i in range(total_notas)]
        media_aluno = calcular_media(notas)
        status_aluno = situacao_status_alunos(media_aluno)
        print(f"O aluno(a) está {status_aluno} com a média {media_aluno:.2f}")

    except ValueError as error:
        print(f"Erro: {error}")
