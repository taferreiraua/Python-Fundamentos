def calcularJuros(inves, juros, saldo):
    mes = 1
    while mes <= 12:
        saldo = round(saldo + (saldo * (juros / 100)) + inves, 2)
        mes = mes + 1
    return round(saldo, 2)


inves = float(input('Investimento mensal: '))
juros = float(input('Juros: '))
saldo = 0

saldo = calcularJuros(inves, juros, saldo)
ano = 1
res = input(f'\nSaldo do investimento após {ano} ano: R${saldo}\nDeseja processar mais um ano?(S/N)\n')
while res.lower() == 's':
    saldo = calcularJuros(inves, juros, saldo)
    ano += 1
    res = input(f'\nSaldo do investimento após {ano} anos: R${saldo}\nDeseja processar mais um ano?(S/N)\n')
