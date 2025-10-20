"""
Módulo de autenticação via terminal.

Solicita ao usuário um nome de usuário e uma senha, e valida a combinação com credenciais pré-definidas.
O processo se repete até que o usuário acerte a combinação correta.
"""

from getpass import getpass

# Credenciais fixas para autenticação
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "senha123"


def autenticar(usuario, senha):
    """
    Verifica se o nome de usuário e a senha correspondem às credenciais corretas.

    Parâmetros:
        usuario (str): Nome de usuário fornecido pelo usuário.
        senha (str): Senha fornecida pelo usuário.

    Retorna:
        bool: True se as credenciais estiverem corretas, False caso contrário.
    """

    return usuario == USUARIO_CORRETO and senha == SENHA_CORRETA


def solicitar_credenciais():
    """
    Solicita ao usuário o nome de usuário e a senha via terminal.

    Retorna:
        tuple: Uma tupla contendo o nome de usuário (str) e a senha (str).
    """
    while True:
        usuario = input("👤 Usuário: ").strip()
        senha = getpass("🔒 Senha: ").strip()
        if usuario and senha:
            return usuario, senha
        print("⚠️  Usuário e senha não podem ser vazios. Tente novamente.")


def acessar_sistema():
    """
    Executa o processo de autenticação em loop até que o usuário acerte a combinação correta.

    Exibe mensagens de acesso concedido ou negado conforme o resultado da verificação.
    """

    print("🔐 Bem-vindo ao sistema de login")
    while True:
        usuario, senha = solicitar_credenciais()
        if autenticar(usuario, senha):
            print("✅ Acesso concedido.")
            break
        print("❌ Acesso negado. Usuário ou senha incorretos.")


def main():
    """
    Função principal que inicia o sistema de autenticação.

    Permite interrupção com Ctrl+C e exibe mensagem apropriada.
    """

    try:
        acessar_sistema()
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")


if __name__ == "__main__":
    main()
