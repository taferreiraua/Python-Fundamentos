def somar(mem, n):
    return mem + n


def subtrair(mem, n):
    return mem - n


def multiplicar(mem, n):
    return mem * n


def dividir(mem, n):
    return mem / n


def limpar_memoria():
    return 0.0


def encerrar():
    print('Encerrando...')


def calculadora(mem, opc, n):
    menu = {1: somar(mem, n),
            2: subtrair(mem, n),
            3: multiplicar(mem, n),
            4: dividir(mem, n),
            5: limpar_memoria(),
            6: encerrar()}
    if 1 <= opc <= 6:
        mem = menu[opc]
    else:
        print(f'\nSELECIONE UMA OPÇÃO VÁLIDA!\n')

    return mem


if __name__ == '__main__':
    mem = 0.0
    n = 1
    opc = 0
    while opc != 6:
        print(f'Estado da memória: {mem}\n'
                  f'Selecione uma opção:\n'
                  f'[1] Somar\n'
                  f'[2] Subtrair\n'
                  f'[3] Multiplicar\n'
                  f'[4] Dividir\n'
                  f'[5] Limpar memória\n'
                  f'[6] Sair do programa')
        opc = int(input(f'------> '))
        if 1 <= opc <= 4:
            n = float(input(f'Digite o valor: '))
        mem = calculadora(mem, opc, n)
