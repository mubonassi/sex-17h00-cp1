import pandas as pd

print("| SISTEMA DE GERENCIAMENTO DE CELULARES |")
print("-"*60)

produtos = {
    "Modelo": ["Poco Phone","S34","G67","iPhone Pro Max Master HD Rumble Remaster Remake"],
    "Marca": ["Xiaomi","Samsung","Motorola","Apple"],
    "OS": ["Android","Android","Android","iOS"]
}

tabela = pd.DataFrame(produtos)
print(tabela)

while True:
    print("# Escolha uma das Opções #")
    print("- 1) Cadastrar")
    print("- 2) Deletar")
    print("- 3) Mostrar Tabela")
    print("- 0) Sair")

    op = input(">> Digite aqui a opção: ")

    match op:
        case "1":
            modelo = input("Digite o nome do modelo: ")
            marca = input("Digite o nome da marca: ")
            os = input("Digite o nome do Sistema Operacional: ")
            tabela.loc[len(tabela)] = [modelo,marca,os]
            print("Cadastrado com sucesso!")
        case "2":
            indice = int(input("Digite o indice do item que deseja deletar: "))
            tabela = tabela.drop(indice).reset_index(drop=True)
            print("Deletado com sucesso! (acho)")
        case "3":
            print(tabela)
        case "0":
            break
    input("Aperte ENTER para continuar...")