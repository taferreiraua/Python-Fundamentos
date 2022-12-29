def preencherVetor():
    res = ''
    vetor = list()
    while res != 'n':
        vetor.append(input('Digite um valor: '))
        res = input('Deseja inserir mais um ítem? (S/N)').lower()
    return vetor


vetor1 = preencherVetor()
vetor2 = preencherVetor()

inter = list()
for a, b in zip(vetor1, vetor2):
    inter.extend([a, b])

print(f'Lista intercalada: {inter + vetor1[len(vetor2):] + vetor2[len(vetor1):]}')
