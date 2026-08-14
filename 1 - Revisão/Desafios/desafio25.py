print("| SOMANDO NÚMEROS NO INTERVALO |")
print("-"*30)

intervalo = int(input("Digite o intervalo de soma da sequência: "))

res = 0
conta = ""
for i in range(1,intervalo+1):
    res += i
    conta += str(i)
    if i < intervalo:
        conta += " + "

print(f"Conta: {conta} = {res}")