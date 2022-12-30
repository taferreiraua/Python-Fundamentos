with open("codigo.py", "w") as arq:
    arq.write('albuns = ["Please Please Me", "With The Beatles", "Beatles For Sale", "A Hard Days Night",\n'
              '"Help!", "Rubber Soul", "Revolver", "Sgt. Peppers Lonely Hearts Club Band", "Magical Mistery Tour"\n'
              '"White Album", "Yellow Submarine", "Abbey Road", "Let it Be"]\n'
              'anoLancamento = [1963, 1963, 1964, 1964, 1965, 1965, 1966, 1967, 1967, 1968, 1969, 1970]\n'
              'for album, ano in zip(albuns, anoLancamento):\n'
              '    print(f"Album: {album}")\n'
              '    print(f"Lançado em: {ano}")')

with open("codigo.py", 'r') as arq:
    linhas = arq.readlines()
    count = 0
    for linha in linhas:
        if 'print' in linha:
            count += 1
    print(f'O arquivo possui {len(linhas)} linhas e {count} prints.')
