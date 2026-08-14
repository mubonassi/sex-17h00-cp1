palavra = input("Digite a palavra que deseja contar os caracteres: ")

cont = 0

for i in palavra:
    cont += 1

print(f"A palavra {palavra} possui {cont} caracteres!")