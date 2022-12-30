with open("nomes.txt", "w") as arq:
    res = ''
    while res != 'n':
       arq.write(input('Nome: ') + '\n')
       res = input('Deseja adicionar outro nome?[S/N]').lower()

with open("nomes.txt", "r") as arqv:
    nomes = arqv.readlines()

with open("nomes_ordenados.txt", "w") as arq_ord:
    for nome in sorted(nomes):
       arq_ord.write(nome)
