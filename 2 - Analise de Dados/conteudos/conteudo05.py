import pandas as pd

dados = {
    "Produto": [
        "Notebook","Monitor","Teclado","Mouse",
        "Headset","Webcam","Notebook","Monitor",
        "Mouse","Teclado","Impressora","Tablet",
        "Celular","Microfone","Caixa de Som",
        "SSD","HD Externo","Pen Drive","Roteador","Switch",
        "Notebook","Monitor","Mouse","Teclado",
        "Headset","Webcam","Impressora","Tablet",
        "SSD","Roteador"
    ],

    "Categoria": [
        "Computador","Monitor","Periférico","Periférico",
        "Áudio","Câmera","Computador","Monitor",
        "Periférico","Periférico","Impressão","Computador",
        "Computador","Áudio","Áudio",
        "Armazenamento","Armazenamento","Armazenamento","Rede","Rede",
        "Computador","Monitor","Periférico","Periférico",
        "Áudio","Câmera","Impressão","Computador",
        "Armazenamento","Rede"
    ],

    "Quantidade": [
        3, 5, 12, 20, 8, 6, 2, 4, 15, 10,
        7, 9, 6, 5, 8, 11, 6, 25, 10, 4,
        5, 8, 18, 14, 9, 7, 3, 6, 12, 8
    ],

    "Valor": [
        4500, 1200, 180, 90, 250, 320, 4500, 1200,
        90, 180, 850, 1500, 2800, 450, 300,
        500, 420, 80, 250, 600,
        5200, 1500, 120, 220, 350, 400, 950, 1800,
        650, 280
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