vet = list()
res = ''
while res != 'n':
    vet.append(int(input('Digite o valor: '))**2)
    res = input('Deseja inserir mais um valor? (S/N)').lower()
print(sum(vet))
