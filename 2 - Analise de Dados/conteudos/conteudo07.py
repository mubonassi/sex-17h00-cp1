import pandas as pd
import matplotlib.pyplot as plt

#Lendo o arquivo e manipulando
tabela = pd.read_csv("dados/produtos.csv")

while True:
    print("1) Gráfico de Barras")
    print("0) Sair")
    
    escolha = input(">> Digite aqui a opção: ")
    
    match escolha:
        case "1":
            campo = input("> Digite o nome do campo para realizar o relatório: ")
            if campo in ["Quantidade","Valor"]:
                plt.figure(figsize=(12,6)) #media em polegadas o x y
                plt.bar(tabela["Produto"],tabela[campo],color="purple",width=0.5,edgecolor="black",linewidth=2)
                
                plt.grid(True)
                plt.grid(axis="y",color="red",linestyle="-")
                plt.grid(axis="x",linestyle="none")
                
                plt.title(f"{campo} de Produtos")
                plt.xlabel("Produtos")
                plt.ylabel(campo)
                plt.xticks(rotation=45)
                plt.tight_layout()
                
                plt.show()
        case "0":
            break