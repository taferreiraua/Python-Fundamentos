frase = input('Digite a frase: ')
mudar = input('Digite a palavra que deseja substituir: ')
novo = input('Digite a palavra nova: ')

frase = frase.split()

for i, palavra in enumerate(frase):
    if palavra == mudar:
        frase[i] = novo

print(frase)
