#Pandas é uma biblioteca utilizada para trabalhar com dados organizados >> EM TABELAS <<
import pandas as pd

#DataFrames
#DataFrame é uma tabela criada pelo Pandas

#Ele é inicialmente estruturado como um objeto com listas
dados = {
    "Nome":["Pedro","Maria","Josivaldo","Xbox"],
    "Idade":[23,45,19,26]
}

tabela = pd.DataFrame(dados)

#Exibindo a tabela de forma completa
print(tabela)
print("-"*60)
#Exibindo uma coluna
print(tabela["Nome"])
print("-"*60)
#Exibindo uma linha especifica
print(tabela.loc[0])
print("-"*60)