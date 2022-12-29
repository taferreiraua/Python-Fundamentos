num = int(input('Dividendo: '))
div = int(input('Divisor: '))
res = 0
aux = div
while div <= num:
    ddiv = num - aux
    res = res + 1
    num = ddiv
print(f'Resultado: {res}\nResto: {num}')
