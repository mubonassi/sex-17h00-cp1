print("Desconto determinado!")
print("-"*30)

valor = float(input("Digite o valor: "))
desconto = float(input("Digite o desconto (%): "))

valor_final = valor - (valor * desconto / 100)

print(f"Valor com desconto: R${valor_final}")
