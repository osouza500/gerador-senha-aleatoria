import secrets
import string

def continuar_sair():
    resposta = input("Criar nova senha? S/N.\n").lower()
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
    comprimento_senha = input("Comprimento da(s) senha(s) (mínimo: 8 caracteres):\n")
    senha = ""
    for contagem in range(int(comprimento_senha)):
        senha += "".join(secrets.choice(alfabeto))
        if (any(caractere in caracteres_especiais for caractere in senha) and
            sum(caractere in digitos for caractere in senha)>=8):
            break
    print(f"Sua senha é '{senha}'.\n")
    continuar_sair()

gerador_senha()