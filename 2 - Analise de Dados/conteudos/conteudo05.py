import pandas as pd

dados = {
    "Produto": [
        "Notebook","Monitor","Teclado","Mouse",
        "Headset","Webcam","Notebook","Monitor",
        "Mouse","Teclado"
        ],

    "Categoria": [
        "Computador","Monitor","Periférico","Periférico",
        "Áudio","Câmera","Computador","Monitor",
        "Periférico","Periférico"
    ],

    "Quantidade": [
        3, 5, 12, 20, 8,6, 2, 4, 15, 10
    ],

    "Valor": [
        4500,1200,180,90,250,320,4500,1200,90,180
    ]
}

tabela = pd.DataFrame(dados)
print(tabela)

#Transformando DataFrame em Arquivo
#1) CSV
#index=False/True -> Se deseja que o indice de cada item seja exportado ou não no arquivo
tabela.to_csv("dados/produtos.csv", index=False)
#2) Excel
tabela.to_excel("dados/produtos.xlsx", index=False)