print("| PARES E IMPARES |")
print("-"*40)

intervalo = int(input("Digite o intervalo que será mostrado: "))

pares = []
for i in range(2,intervalo+1,2):
    pares.append(i)

impares = ""
for i in range(1,intervalo+1,2):
    impares += str(i) + " "

print(f"Pares: {pares}")
print(f"Impares: {impares}")