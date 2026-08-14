import random

print("| JOGO DA PALAVRA MÁGICA |")

palavras = ["Casa","Xbox","Nintendo","67","Praia","Controle","The Legend of Zelda: Ocarina of Time","oi"]
palavraSecreta = random.choice(palavras)

erros = 0

print("- Instruções -")
print("- Digite a sua palavra de tentativa -")
print("- Para desistir escreva: desisto - ")
while True:
    tentativa = input("> Digite aqui: ")

    if tentativa == "desisto":
        print(f"Você DESISTIU! A palavra era: {palavraSecreta}")
        break
    elif tentativa == palavraSecreta:
        print(f"VOCÊ ACERTOUUUUU! ERA REALMENTE {palavraSecreta}!")
        print(f"E você errou {erros} vezes!")
        break
    else:
        erros += 1
        print("ERRRROOOOOOOUUUUUUU!")