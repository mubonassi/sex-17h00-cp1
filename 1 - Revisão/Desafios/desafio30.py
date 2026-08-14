print("| LOJA PYTHON |")
print("-"*60)
produtos = ["Xbox","Playstation","Nintendo","Arroz","Feijão","Funko Pop do Faustão","1 figurinha da copa","Cadeira"]
precos = [3999.99,4500,3800,30,25,10000,20000,50]
pagamentos = ["Pix","Débito","Crédito","Dinheiro","Na Porrada"]

print("-- Lista dos Produtos --")
print(f">> {produtos}")
produto = input("Digite o produto que deseja comprar: ")

if produto in produtos:
    indice = produtos.index(produto)
    preco = precos[indice]

    print(f"| {produto} -- R${preco} |")

    comprar = input("Deseja comprar o produto? (s/n): ").lower()

    if comprar == "s":
        print("-- Formas de Pagamento --")
        print(f">> {pagamentos}")
        pagamento = input("Digite a forma de pagamento: ")

        if pagamento in pagamentos:
            valor = float(input("Digite o quanto está dando do pagamento: "))
            if valor >= preco:
                print(f"Você comprou o produto {produto} utilizando {pagamento}")
            else:
                print("Tá pobre, flw.")
        else:
            print("Forma de pagamento não existente!")
    elif comprar == "n":
        print("Compra cancelada!")
    else:
        print("Sei lá o que cê quis dizer, só irei encerrar esse atendimento. Flw.")
else:
    print("Produto não existente!")