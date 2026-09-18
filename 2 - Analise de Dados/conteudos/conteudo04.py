#CRUD - Os pilares da manipulação de dados
# C - Create - Criação/Inserção de dados
# R - Read - Leitura/Consulta de Dados
# U - Update - Atualização/Modificação de Dados
# D - Delete - Exclusão de Dados

import pandas as pd

dados = {
    "Item": ["A","B","C","D","C"],
    "Valor": [5,10,15,20,25]
}

tabela = pd.DataFrame(dados)
print(tabela)
print("-"*60)

#--CREATE--
#Adicionando uma nova linha
tabela.loc[len(tabela)] = ["E",30]
print(tabela)
print("-"*60)

#Adicionando uma nova COLUNA
tabela["Mês"] = ["Abril","Junho","Dezembro","Setembro","Janeiro","aaaaaaaaaaaaaaaa"]
print(tabela)
print("-"*60)

#--READ--
#Exibindo tabela, coluna, célula e linha
print("Tabela inteira")
print(tabela)
print("Uma coluna")
print(tabela["Item"])
print("Uma linha")
print(tabela.loc[0])
print("Uma célula")
print(tabela.loc[0,"Item"])

#Filtros
#Exibindo uma informação à partir de uma condição
print("-"*60)
print(tabela[tabela["Item"] == "C"])
print(tabela[tabela["Valor"] < 15])
print(tabela[tabela["Valor"] > 20])

#Lembrando os comparadores
# == -> Igual a
# > -> Maior que
# < -> Menor que
# >= -> Maior ou igual a
# <= -> Menor ou igual a
# != -> Diferente de