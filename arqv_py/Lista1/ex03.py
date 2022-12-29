from math import sqrt


x1 = float(input('Ponto 1: \n'
                 'x1: '))
y1 = float(input('y2: '))
x2 = float(input('Ponto 2: \n'
                 'x2: '))
y2 = float(input('y2: '))
print(f'A distância entre os dois pontos é {sqrt((x2-x1)**2 + (y2-y1)**2)}')
