dia, mes, ano = input('Insira uma data (ex.: dd/mm/aaaa): ').split('/')

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
         'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print(f'{dia} de {meses[int(mes)-1]} de {ano}')
