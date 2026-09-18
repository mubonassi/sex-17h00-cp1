import pandas as pd

#Lendo o arquivo e manipulando
tabela = pd.read_csv("dados/produtos.csv")

while True:
    print("-"*60)
    print("1) Mostrar tabela 2) Salvar tabela 3) Salvar excel 4) Salvar tudo")
    print("5) Inserir Registro 6) Deletar Registro 7) Consultar Personalizada")
    print("8) Alterar Produto (Indice) 9) Alterando Produto (pesquisa)")
    print("10) Deletar Registro (pesquisa) 0) Sair")
    print("-"*60)
    escolha = input("Digite aqui a opção: ")
    print("-"*60)
    match escolha:
        case "1":
            print(tabela)
        case "2":
            tabela.to_csv("dados/produtos.csv", index=False)
            print("-- Salvo com Sucesso --")
        case "3":
            tabela.to_excel("dados/produtos.xlsx", index=False)
            print("-- Salvo com Sucesso --")
        case "4":
            tabela.to_csv("dados/produtos.csv", index=False)
            tabela.to_excel("dados/produtos.xlsx", index=False)
            print("-- Salvo com Sucesso --")
        case "5":
            produto = input("Digite o nome do produto: ")
            categoria = input("Digite o nome da categoria: ")
            quantidade = int(input("Digite a quantidade no estoque: "))
            valor = float(input("Digite o valor do produto: "))
            tabela.loc[len(tabela)] = [produto,categoria,quantidade,valor]
            print("-- Inserido com Sucesso --")
        case "6":
            indice = int(input("Digite o indice do item que deseja deletar: "))
            tabela = tabela.drop(indice).reset_index(drop=True)
            print("-- Deletado com Sucesso --")
        case "7":
            campo = input("Digite aqui o campo para realizar a pesquisa: ")
            valor = input("Digite aqui o valor para realizar a pesquisa: ")
            
            if campo in ["Produto","Categoria","Quantidade","Valor"]:
                if campo in ["Quantidade","Valor"]:
                    valor = float(valor)
                item = tabela[tabela[campo] == valor]
                print(item)
        case "8":
            indice = int(input("Digite o indice do produto: "))
            campo = input("Digite qual campo deseja alterar do produto: ")
            valor = input("Digite qual valor à se alterar: ")
            
            if campo in ["Produto","Categoria","Quantidade","Valor"]:
                if campo == "Quantidade":
                    valor = int(valor)
                elif campo == "Valor":
                    valor = float(valor)
                tabela.loc[indice,campo] = valor
                print("-- Alterado com Sucesso --")
            else:
                print("!! Campo não encontrado !!")
        case "0":
            break
    input("Aperte enter para continuar...")