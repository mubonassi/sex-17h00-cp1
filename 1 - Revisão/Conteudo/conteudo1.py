#Revisando Python

#Instruções -> Manipulam, recebem e exibem informações

#Tipos de Informações
#Entrada e Saída -> Define o fluxo da informação
#Informação de Entrada: O Computador RECEBE a informação
#Informação de Saída: O Computador ENVIA a informação

#Exibindo uma informação
#Função print() -> Exibe uma informação no terminal do usuário
print("Hello, World!") #Exibindo o texto "Hello, World"

#Guardando informação + Tipos de Dados
#Variável -> Um espaço na memória do sistema que guarda UMA informação por vez

nome = "Murilo Bonassi" # String -> Texto/Alfanumérico/Caracteres
idade = 32 # Int -> Número Inteiro (0,1,2,3,4...9,10...200...300)
altura = 1.67 # Float -> Número Real (1.0,2.0,3.0...10.15,13.9,77.74)
gosta_de_presunto = False # Boolean (True/False) -> Binário (Sim/Não) (0/1) (Verdadeiro/Falso)
umCalculo = 10+20-30*40/50**60 # Lógico -> Guarda o resultado do comando
frutasFavoritas = ["Maracuja","Amora","Kiwi","Abacaxi"] # Lista -> Array -> Lista de Dados

#Exibindo as variáveis
print("Meu nome é",nome)
print(f"Eu tenho {idade} anos!")
print(f"Eu tenho {altura}m de altura!")
print(f"Se eu gosto de presunto? Isso é {gosta_de_presunto}!")
print(f"10+20-30*40/50**60 = {umCalculo}")
print(f"Frutas Favoritas: {frutasFavoritas}")
print(f"Fruta Favorita: {frutasFavoritas[0]}")

#Recebendo uma informação
#Função input() -> Recebe uma informação EM TEXTO (string) no terminal do usuário
fruta = input("Digite a sua fruta favorita: ")
jogo = input("Digite o seu jogo favorito: ")

print(f"Sua fruta favorita é {fruta}.\nE seu jogo favorito é {jogo}.")