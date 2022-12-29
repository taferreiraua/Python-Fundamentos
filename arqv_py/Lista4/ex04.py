plv = input('Digite uma palavra: ')

vlp = plv[::-1]
if plv == vlp:
    print('A palavra é um palindromo.')
else:
    print('Não é um palindromo.')
