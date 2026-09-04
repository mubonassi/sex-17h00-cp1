print("Complementando o exercício dos produtos!")
print("-"*30)

produto1 = input("Nome do produto 1: ")
valor1 = float(input("Valor do produto 1: "))

produto2 = input("Nome do produto 2: ")
valor2 = float(input("Valor do produto 2: "))

produto3 = input("Nome do produto 3: ")
valor3 = float(input("Valor do produto 3: "))

total = valor1 + valor2 + valor3

print("1 - Débito")
print("2 - Crédito")
print("3 - À Vista")

opcao = int(input("Escolha a forma de pagamento: "))

if opcao == 1:
    valor_final = total

elif opcao == 2:
    valor_final = total + (total * 0.07)

elif opcao == 3:
    valor_final = total - (total * 0.027)

print(f"Valor final: R${valor_final}")
