print("Comprando 3 produtos!")
print("-"*30)

produto1 = input("Nome do produto 1: ")
valor1 = float(input("Valor do produto 1: "))

produto2 = input("Nome do produto 2: ")
valor2 = float(input("Valor do produto 2: "))

produto3 = input("Nome do produto 3: ")
valor3 = float(input("Valor do produto 3: "))

total = valor1 + valor2 + valor3

print(f"{produto1} - R${valor1}")
print(f"{produto2} - R${valor2}")
print(f"{produto3} - R${valor3}")

print(f"Valor total: R${total}")
