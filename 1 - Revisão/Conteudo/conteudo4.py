#Estruturas de Repetição - Estruturas que permitem que blocos de código possam ser executados em loop

#For - Repetição Contada (Determinada)
#i -> variavel contadora
#range() -> determinar a quantidade
for i in range(5):
    print("Teste")
print("Fim da Repetição")

#usar o i no contexto do código
for i in range(5):
    print(f"Repetição {i}")
print("Fim da repetição")

#determinar qual número irá começar na contagem
for i in range(1,6):
    print(f"Rep: #{i}")
print("Fim da repetição")

#determinar qual o intervalo de cada número
for i in range(10,51,10):
    print(f"Rep: #{i}")
print("Fim da repetição")

palavra = "godzilla"
for i in palavra:
    print(i)
print("Fim da repetição")

lista = ["a","bbb","ccccccccc","dddddddddddddd"]
for i in lista:
    print(i)
print("Fim da repetição")