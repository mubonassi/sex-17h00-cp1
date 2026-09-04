print("Festa do Trabalho!")
print("-"*30)

nome = input("Digite seu nome: ")
trabalha = input("Você trabalha na empresa? ")
convite = input("Você possui convite? ")

if trabalha.lower() == "sim" or convite.lower() == "sim":
    print(f"{nome}, você pode entrar na festa!")

else:
    print(f"{nome}, você não pode entrar na festa!")
