print("Algoritmo do Bar!")
print("-"*30)

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome}, você pode entrar no bar!")

else:
    print(f"{nome}, você não pode entrar no bar!")
