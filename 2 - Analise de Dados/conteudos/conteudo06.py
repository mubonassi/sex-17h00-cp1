import pandas as pd

#Lendo o arquivo e manipulando
tabela = pd.read_csv("dados/produtos.csv")

while True:
    print("1) Mostrar tabela 2) Salvar tabela 3) Salvar excel 4) Salvar tudo")
    escolha = input("Digite aqui a opção: ")
    
    match escolha:
        case "1":
            print(tabela)
        case "2":
            tabela.to_csv("dados/produtos.csv", index=False)
        case "3":
            tabela.to_excel("dados/produtos.xlsx", index=False)
        case "4":
            tabela.to_csv("dados/produtos.csv", index=False)
            tabela.to_excel("dados/produtos.xlsx", index=False)