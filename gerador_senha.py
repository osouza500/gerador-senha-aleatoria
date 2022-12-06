import secrets
import string


def continuar_sair():
    resposta = input("Criar nova senha? S/N.\n").lower()
    print("")
    if resposta == "s":
        gerador_senha()
    elif resposta == "n":
        print("Até logo!")
        quit()
    else:
        print("Input inválido. Tente novamente.")
        continuar_sair()


def gerador_senha():
    letras = string.ascii_letters
    digitos = string.digits
    caracteres_especiais = string.punctuation
    alfabeto = letras + digitos + caracteres_especiais
    print("Bem-vind@ ao gerador de senha.\n")
    try:
        comprimento_senha = int(input("Comprimento da senha "
                                      "(mínimo: 8 caracteres):\n"))
        print("")
    except ValueError:
        print("Input inválido. Tente novamente.\n")
        gerador_senha()
    if comprimento_senha < 8:
        print("Input inválido. Tente novamente.\n")
        gerador_senha()
    else:
        while True:
            senha = ""
            for turno in range(comprimento_senha):
                senha += "".join(secrets.choice(alfabeto))
            if any(caractere in caracteres_especiais for caractere in senha):
                break
        print(f"Sua senha é {senha}\n")
        continuar_sair()


if __name__ == "__main__":
    gerador_senha()
