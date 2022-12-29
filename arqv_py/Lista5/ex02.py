res = ''
vetor = list()
while res != 'n':
    vetor.append(int(input('Digite um número: ')))
    res = input('Deseja adicionar mais um número? (S/N)').lower()

media = sum(vetor)/len(vetor)

maiores = list()
menores = list()
for num in sorted(vetor):
    if media <= num:  # pega os valores maiores ou iguais a media
        maiores.append(num)
    if media >= num:  # pega os valores menores ou iguais a media
        menores.append(num)

proxMai = maiores[0]  # menor numero dentre os valores maiores que a media
proxMen = menores[-1]  # maior numero dentre os valores menores que a media

# Compara a diferença entre proxMai e proxMen (usando modulo)
#  1) Se existirem dois numeros igualmente proximos á media:
if abs(proxMai - media) == abs(proxMen - media) and proxMen != proxMai:
    print(f'Valores mais próximos da média: {proxMen}, {proxMai}')
#  2) Se o numero da media estiver presente no vetor:
elif proxMai == proxMen:
    print(f'Valor mais próximo da média: {proxMai}')
#  3) Se a distancia de proxMai/media for maior que a de prox3/media:
elif abs(proxMai - media) > abs(proxMen - media):
    print(f'Valor mais próximo da média: {proxMen}')
#  4) Se a distancia de prox3/media for maior que a de prox2/media:
elif abs(proxMai - media) < abs(proxMen - media):
    print(f'Valor mais próximo da média: {proxMai}')
