from dados2 import torradeiras as tdb

def mostrardado(dado):
    print(f"Marca: {dado['marca']}")
    print(f"Fatias: {dado['fatias']}")
    print(f"Potencia: {dado['potencia']}")
    print("-"*40)

print("| SISTEMA DE TORRADEIRAS |")

while True:
    print("> Escolha uma das ferramentas (pelo indice numérico)")
    print("1) Mostrar todos os dados")
    print("2) Pesquisar pela marca (dado exato)")
    print("3) Pesquisar pela marca (parte do dado)")
    print("4) Sair")

    op = input(">> Digite a opção desejada: ")
    print("-"*40)
    match op:
        case "1":
            for t in tdb:
                mostrardado(t)
            input("Aperte enter para continuar...")
        case "2" | "3":
            valor = input("Digite o nome da marca: ")
            pesquisa = False
            for t in tdb:
                if op == "2" and valor.lower() == t['marca'].lower():
                    mostrardado(t)
                    pesquisa = True
                if op == "3" and  valor.lower() in t['marca'].lower():
                    mostrardado(t)
                    pesquisa = True
            if pesquisa == False:
                print("Nenhum foi encontrado!")
            input("Aperte enter para continuar...")
        case "4":
            break
    print("-"*40)