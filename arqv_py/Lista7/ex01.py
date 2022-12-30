with open("frase.txt", "w") as arq:
    arq.write(input('Digite a frase: '))

with open("frase.txt", "r") as arq:
    print(arq.read())
