num = int(input("Digite um número: "))

if num == 0:
    fibon = '[0]'
elif num == 1:
    fibon = '[0, 1]'
else:
    fibon = list()
    fibon.extend([0, 1, 1])
    ultimo = 1
    penultimo = 1
    for i in range(2, num):
        prox = ultimo + penultimo
        penultimo = ultimo
        ultimo = prox
        i += 1
        fibon.append(prox)

print(f'A série fibonnaci para esse número é {fibon}')
