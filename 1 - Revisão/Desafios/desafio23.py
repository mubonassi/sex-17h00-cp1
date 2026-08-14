tabuada = int(input("Digite o número que queira realizar tabuada: "))

for i in range(1,11):
    res = tabuada * i
    print(f"{tabuada} x {i} = {res}")