def fatorial(num):
    fat = 1
    while num != 1:
        fat = fat * num
        num = num - 1
    return fat


def combinacao(num_m, num_n):
    n = fatorial(num_m)
    m = fatorial(num_n)
    mn = fatorial(num_m - num_n)
    comb = n / (m * mn)
    return comb


if __name__ == '__main__':
    n = int(input('Total de alunos: '))
    m = int(input('Digite o numero de pessoas do 1° grupo: '))

    print(f'Numero de combinações: {combinacao(n, m)}')
