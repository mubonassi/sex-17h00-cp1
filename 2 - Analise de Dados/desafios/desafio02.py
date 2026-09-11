import pandas as pd

print("| SISTEMA DE GERENCIAMENTO DE ESCAVADEIRAS |")

dados = {
    "Marca": [
        "Caterpillar", "Komatsu", "Volvo", "JCB", "Hyundai",
        "John Deere", "Liebherr", "Case", "Doosan", "Hitachi"
    ],
    "Modelo": [
        "320", "PC210", "EC220", "JS220", "HX220",
        "210G", "R 922", "CX210", "DX225", "ZX210"
    ],
    "Valor": [
        850000, 720000, 780000, 690000, 710000,
        750000, 920000, 680000, 730000, 800000
    ],
    "Tamanho": [
        "Grande", "Grande", "Grande", "Médio", "Grande",
        "Grande", "Grande", "Médio", "Grande", "Grande"
    ]
}

tabela = pd.DataFrame(dados)

while True:
    print("-"*60)
    print("-- Menu Principal --")
    print("1) Pesquisar por marca (especifico)")
    print("2) Pesquisar por modelo (parte)")
    print("3) Pesquisar por valor (>=)")
    print("4) Extra: Pesquisa Personalizada")
    print("5) Exibir Tabela Inteira")
    print("0) Sair")

    op = input(">> Digite aqui a opção: ")
    match op:
        case "1":
            valor = input("> Digite a marca: ")
            item = tabela[tabela["Marca"] == valor]
            print(item)
        case "2":
            valor = input("> Digite o modelo: ")
            for item in tabela["Modelo"]:
                if valor in item:
                    print(tabela[tabela["Modelo"] == item])
        case "3":
            try:
                valor = float(input("> Digite o valor: "))
                item = tabela[tabela["Valor"] >= valor]
                print(item)
            except:
                print("Digite um valor correto!")
        case "4":
            print("-- Escolha um dos campos: Marca, Modelo, Valor ou Tamanho")
            campo = input(">> Digite aqui: ")
            if campo.capitalize() in ["Marca","Modelo","Valor","Tamanho"]:        
                valor = input(f">> Digite o valor do {campo}: ")

                if campo == "Valor":
                    valor = float(valor)
                
                item = tabela[tabela[campo] == valor]
                print(item)
            else:
                print("Escolha um campo correto!")
        case "5":
            print(tabela)
        case "0":
            break
    input("Aperte enter para continuar...")