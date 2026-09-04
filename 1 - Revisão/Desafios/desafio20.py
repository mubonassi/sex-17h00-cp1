print("Posto de Pythonlina!")
print("-"*30)

tanque = float(input("Digite o tamanho do tanque: "))
atual = float(input("Quantos litros já tem no tanque? "))
abastecer = float(input("Quantos litros deseja abastecer? "))
preco = float(input("Digite o valor do litro: "))

totalAbastecido = atual + abastecer

if totalAbastecido <= tanque:
    total = abastecer * preco

    print(f"Valor total: R${total}")

    pagamento = float(input("Quanto dinheiro será pago? "))

    if pagamento >= total:
        troco = pagamento - total
        print(f"Pagamento realizado com sucesso!")
        print(f"Troco: R${troco}")

    else:
        print("Dinheiro insuficiente!")

else:
    print("Você ultrapassou o limite do tanque!")
