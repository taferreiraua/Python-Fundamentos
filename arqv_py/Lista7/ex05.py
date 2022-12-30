with open("trecho.txt", "w") as arq:
    arq.write('Bem me recordo! Era em dezembro. Um frio atroz, ventos cortantes...\n'
              'Morria a chama no fogão, pondo no chão sombras errantes.\n'
              'Eu nos meus livros procurava - ansiando as horas matinais -\n'
              'um meio (em vão) de amortecer fundas saudades de Lenora,\n'
              '- bela adorada, a quem, no céu, os querubins chamam Lenora,\n'
              'e aqui, ninguém chamará mais.')

with open("trecho.txt", "r") as arq:
    linhas = arq.readlines()

with open("q5_trecho.txt", "w") as arqv:
    for i in range(3, 6, 1):
        arqv.write(linhas[i])
