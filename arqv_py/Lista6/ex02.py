from numpy import mean


def status(media):
    if media >= 6:
        return f'Status: Aprovado.'
    elif 4 <= media < 6:
        return f'Status: Verificação Suplementar.'
    elif media < 4:
        return f'Status: Reprovado.'


if __name__ == '__main__':
    res = ''
    notas = list()
    while res != 'n':
        notas.append(int(input('Digite a nota: ')))
        res = input('Deseja inserir outra nota? (S/N)').lower()

    media = mean(notas)
    status = status(media)
    print(status)
