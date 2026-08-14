#Repetição condicionada
#While

#O código irá se repetir até a condição não for mais verdadeira
numero = 0
while numero == 0:
    numero = int(input("Digite um número diferente de 0 (zero): "))
    print(f"Você digitou: {numero}")

#Repetição indefinida
while True:
    escolha = input("Deseja finalizar o código? (s/n): ").lower()
    if escolha == "s":
        break