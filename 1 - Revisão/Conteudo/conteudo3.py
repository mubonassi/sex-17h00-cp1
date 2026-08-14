#Estruturas de Condição
#IF -> Verificadores -> Verifica uma condição antes de executar um bloco de comando

#comparadores
# == -> Igual a -> valor == valor
# > -> Maior que -> valor > valor
# >= -> Maior ou igual a -> valor >= valor
# < -> Menor que -> valor < valor
# <= -> Menor ou igual a -> valor <= valor
# != -> Diferente de -> valor != valor

numero = int(input("Digite um número para ser verificado: "))

#condição simples
if numero > 5:
    print("Você digitou um número maior que 5")
else:
    print("Você NÃO digitou um número maior que 5")

#condição composta
#utilizando multiplas condições (AND e OR)
#or -> uma das condições necessitam ser verdadeiras
if numero == 6 or numero == 9:
    print("Você digitou um dos números secretos")
else:
    print("Você não digitou um dos números secretos")

#and -> todas as condições necessitam ser verdadeiras
if numero >= 0 and numero <= 10:
    print("Você digitou um número entre 0 a 10")
else:
    print("Você não digitou um número entre 0 a 10")

#condição encadadeada
#utilizando multiplas estruturas/perguntas
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Neutro")

#condição na lista
#usando o comparador in e not in
lista = ["a","b","c","d","e"]

item = "a"
item2 = "f"

print(lista)
if item in lista:
    print(f"item {item} existente!")

if item2 not in lista:
    print(f"item {item2} não está na lista!")