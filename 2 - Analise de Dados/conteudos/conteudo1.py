#Dados
valor = "Informação"
print(valor)
lista = ["A","B","C","D","E","F"]
print(lista)

#Objetos
pessoa = {
    "nome":"Murilo",
    "idade":25,
    "altura":1.68
}
print(pessoa)
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Altura: {pessoa['altura']}")

#Lista de Objetos
pessoas = [
    {
        "nome":"Fernando",
        "idade":87,
        "altura":1.10
    },
    {
        "nome":"Thyagho",
        "idade":13,
        "altura":1.99
    },
    {
        "nome":"Pikachu",
        "idade":30,
        "altura":1.05
    },
    {
        "nome":"Rogisnaldo",
        "idade":45,
        "altura":1.80
    }
]

for p in pessoas:
    print("-"*40)
    print(f"Nome: {p['nome']}")
    print(f"Idade: {p['idade']}")
    print(f"Altura: {p['altura']}")