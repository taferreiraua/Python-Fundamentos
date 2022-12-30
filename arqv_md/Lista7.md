# Manipulação de arquivos

### **Questão 1:**
> **_Faça um programa que escreve uma frase digitada pelo usuário em um arquivo. Em
seguida, o programa deve ler e imprimir o conteúdo desse arquivo._**

---
```python
with open("frase.txt", "w") as arq:
    arq.write(input('Digite a frase: '))

with open("frase.txt", "r") as arq:
    print(arq.read())
```
---

### **Questão 2:**
> **_Escreva um programa que lê um arquivo contendo a identidade e o nome de várias
pessoas, no seguinte formato:_**
> <br/> **_5384423 Manoel_**
> <br/> **_4345566 Alberto_**
> <br/> **_3235574 Mariana_**
> <br/> **_O programa deve gerar um dicionário onde as chaves são as identidades e os valores
os nomes. Ao final o programa deve exibir o dicionário._**

---
```python
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
```
---

### **Questão 3:**
> **_Escreva um programa que lê um arquivo contendo endereços IPs, da seguinte forma:_**
> <br/> **_200.135.80.9_**
> <br/> **_192.168.1.1_**
> <br/> **_8.35.67.74_**
> <br/> **_257.32.4.5_**
> <br/> **_85.345.1.2_**
> <br/> **_1.2.3.4_**
> <br/> **_9.8.234.5_**
> <br/> **_192.168.0.256_**
> <br/> **_O programa deve mostrar os IPS indicando os que são válidos e inválidos (um
endereço ip válido não pode ter uma de suas partes maior que 224)._**

---
```python
with open("IPs.txt", "w") as ips:
    ips.write('200.135.80.9\n'
              '192.168.1.1\n'
              '8.35.67.74\n'
              '257.32.4.5\n'
              '85.345.1.2\n'
              '1.2.3.4\n'
              '9.8.234.5\n'
              '192.168.0.256')

with open("IPs.txt", "r") as arq:
    ips = arq.readlines()
    for ip in ips:
        for num in ip.strip('\n').split('.'):
            if int(num) > 224:
                print(ip)
```
---

### **Questão 4:**
> **_Escreva um programa que leia um arquivo com um conjunto de nomes (1 por linha).
O programa deve ordenar os nomes e gerar um novo arquivo com os nomes
ordenados._**

---
```python
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
```
---

### **Questão 5:**
> **_Faça um programa que leia as linhas de 3 a 5 de um arquivo de texto (considere que
tem mais do que 5 linhas). Copie as linhas selecionadas em um novo arquivo._**

---
```python
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
```
---

### **Questão 6:**
> **_Escreva um programa que leia um arquivo em python (nome fornecido pelo usuário).
O programa deverá informar: (i) Quantas linhas o arquivo tem e (ii) A quantidade de
“print” que o código possui._**

---
```python
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
```
---
