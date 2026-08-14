print("| CALCULADORA COMPLETA |")
print("-"*40)

operadores = ["+","-","/","**","//","%"]

print("-- Digite os dois números que vão operar")
n1 = float(input("Digite aqui o N1: "))
n2 = float(input("Digite aqui o N2: "))

print(f"-- Escolha um dos operadores: {operadores}")
op = input("Digite aqui: ")

if op not in operadores:
    print("!ERRO! Operador inválido!")
    quit()
elif (op == "/" or op == "//" or op == "%") and (n2 == 0):
    print("!ERRO! Não se pode dividir por zero!")
    quit()

if op == "+":
    resultado = n1+n2
elif op == "-":
    resultado = n1-n2
elif op == "/":
    resultado = n1/n2
elif op == "*":
    resultado = n1*n2
elif op == "**":
    resultado = n1**n2
elif op == "//":
    resultado = n1//n2
elif op == "%":
    resultado = n1%n2

print("-- CONTA --")
print(f"{n1} {op} {n2} = {resultado}")