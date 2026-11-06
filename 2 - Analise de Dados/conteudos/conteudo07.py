import pandas as pd
import matplotlib.pyplot as plt

def grafPizza(tabela):
    cores = ["purple","pink","red","orange","yellow"]
    destaques = []
    campo = input("> Digite o nome do campo para realizar o relatório: ")
    if campo in ["Quantidade","Valor"]:
        #pesquisa = tabela.head(5)
        pesquisa = tabela.nlargest(5,campo)
        maiorValor = pesquisa[campo].max()
        
        for prod in pesquisa[campo]:
            if prod == maiorValor:
                destaques.append(0.2)
            else:
                destaques.append(0)
        
        plt.pie(pesquisa[campo],labels=pesquisa["Produto"],colors=cores,explode=destaques)
        plt.title(f"{campo} dos Produtos")
        
        plt.show()

def grafLinhas(tabela):
    campo = input("> Digite o nome do campo para realizar o relatório: ")
    if campo in ["Quantidade","Valor"]:
        plt.plot(tabela["Produto"], tabela[campo], color="pink",linewidth=3,linestyle="-",marker="*", markersize=15,markerfacecolor="red",markeredgecolor="pink")
        plt.title(f"{campo} dos Produtos")
        plt.xlabel("Registros")
        plt.ylabel(campo)
        plt.xticks(rotation=90)

        plt.tight_layout()
        
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

def filtrar():
    try:
        filtro = input("> Digite se a pesquisa será de valor maior '>' ou menor '<': ")
        campo = input("> Digite qual o campo para realizar a pesquisa: ")
        valor = int(input("> Digite o valor da pesquisa: "))
        
        if filtro in [">","<"] and campo in ["Quantidade","Valor"] and valor > 0:
            if filtro == ">":
                pesquisa = tabela[tabela[campo] >= valor]
            else:
                pesquisa = tabela[tabela[campo] <= valor]
            return pesquisa
        else:
            print("ERRO: Não sei o que, mas conserta aí. Boa sorte.")
            return False
    except:
        print("ERRO: Algo cabuloso. Não sei. Mas impedi de dar zika.")
        return False

#Lendo o arquivo e manipulando
tabela = pd.read_csv("dados/produtos.csv")

while True:
    print("-- Relatório Geral --")
    print("1) Gráfico de Barras; 2) Gráfico de Linhas 3) Gráfico de Pizza 4) Group By")
    print("-- Relatório Especifico --")
    print("1.5) Gráfico de Barras 2.5) Gráfico de Linhas 3.5) Gráfico de Pizza")
    print("-- Gráfico com Group By --")
    print("4.1) Gráfico de Barras 4.2) Gráfico de Linhas 4.3) Gráfico de Pizza ")
    print("0) Sair")
    
    escolha = input(">> Digite aqui a opção: ")
    
    match escolha:
        case "1":
            grafBarra(tabela)
        case "1.5":
            pesquisa = filtrar()
            if pesquisa is not False:
                grafBarra(pesquisa)
        case "2":
            grafLinhas(tabela)
        case "2.5":
            pesquisa = filtrar()
            if pesquisa is not False:
                grafLinhas(pesquisa)
        case "3":
            grafPizza(tabela)
        case "3.5":
            pesquisa = filtrar()
            if pesquisa is not False:
                grafPizza(tabela)
        case "4":
            relatorio = tabela.groupby("Categoria")["Quantidade"].sum() #Sum -> Soma
            print("- Total de Estoque por Categoria -")
            print(relatorio)
            
            relatorio = tabela.groupby("Categoria")["Valor"].mean() #Mean -> Média
            print("- Média de Valor por Categoria -")
            print(relatorio)
        case "0":
            break
        case _:
            print("ERRO: Escolha uma opção correta!")
    input("Aperte enter para continuar...")