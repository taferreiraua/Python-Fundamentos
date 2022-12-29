num = int(input('Digite um número: '))
i = 1
while i * (i+1) * (i+2) < num:
    i = i + 1
if i * (i+1) * (i+2) == num:
    print(f'{num} é o produto de {i} x {i+1} x {i+2}')
else:
    print(f'{num} não é produto de inteiros consecutivos.')
