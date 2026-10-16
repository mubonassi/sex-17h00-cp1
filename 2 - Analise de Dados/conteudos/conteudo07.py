import pandas as pd
import matplotlib.pyplot as plt

def grafLinhas(tabela):
    campo = input("> Digite o nome do campo para realizar o relatório: ")
    if campo in ["Quantidade","Valor"]:
        plt.plot(tabela.index, tabela[campo], color="pink",linewidth=3,linestyle="-")
        plt.title(f"{campo} dos Produtos")
        plt.xlabel("Registros")
        plt.ylabel(campo)
        
        plt.show()

def grafBarra(tabela):
    campo = input("> Digite o nome do campo para realizar o relatório: ")
    if campo in ["Quantidade","Valor"]:
        plt.figure(figsize=(12,6)) #media em polegadas o x y
        relatorio = plt.bar(tabela["Produto"],tabela[campo],color="purple",width=0.5,edgecolor="black",linewidth=2)
        
        plt.grid(True)
        plt.grid(axis="y",color="red",linestyle="-")
        plt.grid(axis="x",linestyle="none")
        
        plt.title(f"{campo} de Produtos")
        plt.xlabel("Produtos")
        plt.ylabel(campo)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.bar_label(relatorio, padding=3)
        
        plt.show()

#Lendo o arquivo e manipulando
tabela = pd.read_csv("dados/produtos.csv")

while True:
    print("-- Relatório Geral --")
    print("1) Gráfico de Barras; 2) Gráfico de Linhas")
    print("-- Relatório Especifico --")
    print("1.5) Gráfico de Barras")
    print("0) Sair")
    
    escolha = input(">> Digite aqui a opção: ")
    
    match escolha:
        case "1":
            grafBarra(tabela)
        case "1.5":
            try:
                filtro = input("> Digite se a pesquisa será de valor maior '>' ou menor '<': ")
                campo = input("> Digite qual o campo para realizar a pesquisa: ")
                valor = int(input("> Digite o valor da pesquisa: "))
                
                if filtro in [">","<"] and campo in ["Quantidade","Valor"] and valor > 0:
                    if filtro == ">":
                        pesquisa = tabela[tabela[campo] >= valor]
                    else:
                        pesquisa = tabela[tabela[campo] <= valor]
                    grafBarra(pesquisa)
                else:
                    print("ERRO: Não sei o que, mas conserta aí. Boa sorte.")
            except:
                print("ERRO: Algo cabuloso. Não sei. Mas impedi de dar zika.")
        case "2":
            grafLinhas(tabela)
        case "0":
            break
        case _:
            print("ERRO: Escolha uma opção correta!")
    input("Aperte enter para continuar...")