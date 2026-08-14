import random

print("| SOMANDO/SUBTRAINDO ATÉ O VALOR CORRETO!")
print("-"*60)

objetivo = random.randint(1,100)
total = 0
op = "adicionar"

print("- Instruções -")
print("- Digite valores que irão SOMAR ou SUBTRAIR dentro do total até acertar o objetivo -")
print("- Digite 0 para desistir e receber o total -")
while total != objetivo:
    print()
    tentativa = int(input(f"Digite o valor para {op}: "))

    if tentativa == 0:
        print("Você DESISTIU!!!!!!111")
        print(f"O valor era {objetivo}!")
        break
    elif op == "adicionar":
        total += tentativa
    elif op == "subtrair":
        total -= tentativa

    if total == objetivo:
        print(f"VOCÊ ACERTOU! O VALOR ERA {objetivo}!")
        break
    elif total > objetivo:
        print("O valor agora está ACIMA do objetivo!")
        op = "subtrair"
    elif total < objetivo:
        print("O valor agora está ABAIXO do objetivo!")
        op = "adicionar"