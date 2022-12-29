vetor = list()
posipar = 0
posimpar = 0

#  Calculando o valor de cada fração
for i in range(1, 1000000, 2):
    inter = 1/i
    vetor.append(inter)

for j in range(500000):
    if j % 2 == 0:  # Somando os valores em posição par
        posipar += vetor[j]
    else:  # Somando os valores em posição ímpar
        posimpar += vetor[j]

pi = (posipar - posimpar)*4
print(pi)
