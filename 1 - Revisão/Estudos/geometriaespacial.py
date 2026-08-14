print("RAIZ QUADRADA!!!!!!!!11111")
valor = int(input("Digite um valor: "))
raiz = valor ** 0.5

if raiz != int(raiz):
    print("Irracional")
    print(f"√{valor}")
else:
    print(f"Raiz deu: {raiz}")