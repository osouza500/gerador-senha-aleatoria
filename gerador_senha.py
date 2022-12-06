import secrets
import string 

letras = string.ascii_letters
digitos = string.digits
caracteres_especiais = string.punctuation

alfabeto = letras + digitos + caracteres_especiais

# quantidade_senha = input("Quantidades de senha que deseja criar:\n")
comprimento_senha = input("Comprimento da senha (em caracteres):\n")

senha = ""

for contagem in range(int(comprimento_senha)):
    senha += "".join(secrets.choice(alfabeto))

print(senha)