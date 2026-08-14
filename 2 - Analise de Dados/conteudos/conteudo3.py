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

#Consultando dados
#Exibindo uma coluna
print(tabela["Nome"])
print("-"*60)

#Exibindo uma linha especifica
print(tabela.loc[0])
print("-"*60)

#Exibindo uma célula específica
#Linha 0, coluna "Nome"
#loc[x,y] -> X: a linha; Y: a coluna
print(tabela.loc[2,"Nome"])

#Alterar e adicionar valores
#Alterando
tabela.loc[3,"Nome"] = "Jorisvaldo"

#Adicionar uma nova linha
tabela.loc[4] = ["Roberto Carlos",87]

#Adicionando na PRÓXIMA linha disponível
#Utilizando a função len()
tabela.loc[len(tabela)] = ["Próximo Nome",300]

#Deletando uma linha da tabela
#Utilizando drop()
tabela = tabela.drop(2)

print(tabela)