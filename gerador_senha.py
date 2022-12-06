import secrets
import string
import time

letras = string.ascii_letters
digitos = string.digits
caracteres_especiais = string.punctuation

alfabeto = letras + digitos + caracteres_especiais

# quantidade_senha = input("Quantidades de senha que deseja criar:\n")
comprimento_senha = input("Comprimento da senha (mínimo):\n")

senha = ""

for contagem in range(int(comprimento_senha)):
    senha += "".join(secrets.choice(alfabeto))

if (any(caractere in caracteres_especiais for caractere in senha) and
    sum(caractere in digitos for caractere in senha)>=6):
        break

print(senha)