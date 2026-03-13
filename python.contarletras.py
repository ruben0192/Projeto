fase = input("Digite uma frase: ")
quantidade_letras = 0

if len(fase) > 20:
    print("A frase é muito grande")

for caractere in fase:
    if caractere.isalpha():
        quantidade_letras += 1

print(f"A frase tem {quantidade_letras} letras.")
