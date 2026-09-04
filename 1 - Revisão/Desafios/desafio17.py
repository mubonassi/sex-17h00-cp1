print("Senha Numérica!")
print("-"*30)

senha = 50

tentativa = int(input("Digite a senha: "))

if tentativa == senha:
    print("Senha correta!")

elif tentativa > senha:
    print("Você digitou um número maior que a senha!")

else:
    print("Você digitou um número menor que a senha!")
