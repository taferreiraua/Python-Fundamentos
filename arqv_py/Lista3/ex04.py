num = int(input('Digite um número: '))
ndiv = 0

for div in range(num, 0, -1):
    if num % div == 0:
        res = round(num / div)
        ndiv = ndiv + 1
        print(f'{num}/{div} = {res}')
if ndiv == 2:
    print('O numero é primo.')
