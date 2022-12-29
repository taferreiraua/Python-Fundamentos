from math import sqrt


def circunferencia(raio):
    peri = round(2 * 3.14 * raio, 2)
    area = round(3.14 * raio * raio, 2)
    return f'Area = {area}\nPerimetro = {peri}'


def triang_isosceles(l1, l2, base):
    peri = round(l1 + l2 + base, 2)
    area = round(base * ((l1*l1) - (l2*l2 / 4)) / 2, 2)
    return f'Area = {area}\nPerimetro = {peri}'


def triang_escaleno(l1, l2, l3):
    peri = round(l1 + l2 + l3/3, 2)
    area = round(sqrt(peri*(peri - l1)*(peri - l2)*(peri - l3)), 2)
    return f'Area = {area}\nPerimetro = {peri}'


def triang_equilatero(l1, l2, l3):
    peri = round(l1 + l2 + l3, 2)
    area = round(l1*l1*sqrt(3)/4, 2)
    return f'Area = {area}\nPerimetro = {peri}'


def retangulo(base, altu):
    peri = round(base * altu, 2)
    area = round(2 * (base + altu), 2)
    return f'Area = {area}\nPerimetro = {peri}'


if __name__ == '__main__':
    opc = 1
    while opc != 0:
        opc = int(input(f'Figura:\n[1] Circunferencia\n[2] Triângulo\n[3] Retângulo\nDigite 0 para sair-----> '))
        if opc == 1:
            print(circunferencia(float(input('Raio: '))))
        elif opc == 2:
            res = int(input('Informe o tipo do triâgulo:\n[1] Isosceles\n[2] Escaleno\n[3] Equilátero\n\t-----> '))
            l1 = float(input('Lado 1: '))
            l2 = float(input('Lado 2: '))
            l3 = float(input('Lado 3: '))
            menu = {1: triang_isosceles(l1, l2, l3),
                    2: triang_escaleno(l1, l2, l3),
                    3: triang_equilatero(l1, l2, l3)}
            print(menu[res])
        elif opc == 3:
            print(retangulo(float(input('Base: ')), float(input('Altura: '))))
        elif opc > 3 or opc < 0:
            print('\nDIGITE UMA OPÇÃO VÁLIDA!')
