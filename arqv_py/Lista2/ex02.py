print('Informe as medidas do triangulo\n')
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1: # Em qualquer triângulo, cada lado é menor que a soma dos outros dois lados
    print('Não é um triângulo.')
elif l1 == l2 == l3:
    print('É um equilátero.')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('É um isosceles.')
else:
    print('É um escaleno.')
