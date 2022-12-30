with open("nomes.txt", "a") as arq:
    res = ''
    while res != 'n':
       arq.write(input('ID: ') + ' ')
       arq.write(input('Nome: ') + '\n')
       res = input('Deseja adicionar outra pessoa?[S/N]').lower()

with open("nomes.txt", "r") as arquivo:
    listaNomes = arquivo.readlines()
    dic = dict()
    for string in listaNomes:
        pessoa = string.split()
        dic[pessoa[0]] = pessoa[1]

id = input('Procurar ID: ')
print(dic.get(id))
