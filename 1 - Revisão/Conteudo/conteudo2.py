#Processando e Calculando Informações

#Exemplo 1 - Criando o nome completo
#Calculando Strings
nome = input("Digite aqui o seu nome: ")
sobrenome = input("Digite aqui o seu sobrenome: ")
nomeCompleto = nome + " " + sobrenome

print(f"Seu nome completo é: {nomeCompleto}")

#Exemplo 2 - Somando Dois Números
#Calculando Numeros -> Necessita conversão (int/float)
numero1 = int(input("Digite o numero #1: "))
numero2 = float(input("Digite o numero #2: "))
soma = numero1 + numero2
print(f"{numero1} + {numero2} = {soma}")