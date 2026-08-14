#Funções - São blocos de código que devem ser chamados para serem executados
#print()
#variavel = input()

#def -> cria uma função de script (criada pelo dev)

#Funções Simples -> Apenas executam o comando dentro
def exibirTexto():
    print("Oi, eu sou um texto")
exibirTexto()

def somarDoisNumeros():
    valor1 = 1
    valor2 = 2
    resultado = valor1+valor2
    print(f"Resultado: {resultado}")
somarDoisNumeros()

#Funções Simples com Return -> Executam comando e retornam um valor
#Necessita de uma variavel ou qualquer outro comando que receba o valor
def subtrairDoisNumeros():
    valor1 = 300
    valor2 = 50
    resultado = valor1-valor2
    return resultado

res = subtrairDoisNumeros()
print(f"Resultado deu: {res}")

#Funções com parametro -> Necessitam de valores externos para realizar o comando
def multiplicarDoisNumeros(valor1,valor2):
    resultado = valor1*valor2
    return resultado

res = multiplicarDoisNumeros(10,20)
print(f"Resultado deu: {res}")