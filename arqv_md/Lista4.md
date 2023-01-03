# Manipulação de Strings

### **Questão 1:**
 **Escreva um programa que lê uma frase, uma palavra antiga e uma palavra nova. O
programa deve imprimir a frase com as ocorrências da palavra antiga substituídas pela
palavra nova. Por exemplo:**
 - **Frase: “Quem parte e reparte fica com a maior parte”**
 - **Palavra antiga: “parte”**
 - **Palavra nova: “parcela”**
 - **Saída: “Quem parcela e reparte fica com a maior parcela”**

### **Resolução:**
> **_Usamos a função `split()`, que retorna uma lista onde cada elemento é uma
> palavra da string. Em seguida a percorremos usando o `enumerate()`, que
> retorna uma tupla de dois elementos a cada iteração: um número sequencial e um item da sequência correspondente._**

---
```python
frase = input('Digite a frase: ')
mudar = input('Digite a palavra que deseja substituir: ')
novo = input('Digite a palavra nova: ')

frase = frase.split()

for i, palavra in enumerate(frase):
    if palavra == mudar:
        frase[i] = novo

print(frase)
```
---

### **Questão 2:**
 **Faça um programa que lê uma frase e retorna o número de palavras que a frase
contém. Considere que a palavra pode começar e/ou terminar por espaços.**

### **Resolução:**
> **_Usamos a função `split()` para retornar uma lista com cada palavra da frase, 
> e usamos o `len()` para retornar a quantidade de elemento._**

---
```python
frase = input('Digite a frase: ')

plv = frase.split()

print(f'Há {len(plv)} palavras nesta frase.')
```
---

### **Questão 3:**
 **Faça um programa que recebe uma frase e substitui todas as ocorrências de espaço por
“#”.**

### **Resolução:**
> **_A função `replace()` substitui trechos de uma string._**

---
```python
frase = input('Digite uma frase: ')

print(frase.replace(' ', '#'))
```
---

### **Questão 4:**
 **Faça um programa que decida se duas strings lidas do teclado são palíndromas
mútuas, ou seja, se uma é igual à outra quando lida de trás para frente. Exemplo:
amor e roma.**

### **Resolução:**

> **_Simples: usamos uma notação slice para reverter a string e comparar com a string
> original._**

---
```python
plv = input('Digite uma palavra: ')

if plv == plv[::-1]:
    print('A palavra é um palindromo.')
else:
    print('Não é um palindromo.')
```
---

### **Questão 5:**
 **Um anagrama é uma palavra que é feita a partir da transposição das letras de outra
palavra ou frase. Por exemplo, “Iracema” é um anagrama para “America”. Escreva
um programa que decida se uma string é um anagrama de outra string, ignorando os
espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo
caracteres iguais, ou seja, “a” = “A”.**

### **Resolução:**

> **_Definimos a função `isanagrama()` que recebe como parâmetro duas palavras e retorna
> `True`, se as palavras são anagramas, e `False` caso contrário. Tranformamos as duas palavras
> em listas, onde cada elemento é uma letra da palavra e depois ordenamos as letras, para
> facilitar a verificação._**

---
```python
def isanagrama(plv1: str, plv2: str):
    plv1 = list(plv1)
    plv2 = list(plv2)

    plv1.sort()
    plv2.sort()

    if plv1 == plv2:
        return True
    else:
        return False


plv1 = input('Digite uma palavra: ').upper().strip()
plv2 = input('Digite outra palavra: ').upper().strip()

if isanagrama(plv1, plv2) is True:
    print('É um anagrama.')
else:
    print('Não é um anagrama.')
```
---


### **Questão 6:**
 **Faça um programa que leia o nome do usuário e mostre o nome de trás para frente,
utilizando somente letras maiúsculas. Exemplo: Nome = Vanessa. Resultado gerado
pelo programa: ASSENAV.**

**_Simples: usamos um slice inverso, para inverter a string, e a função `upper()` para
converter as letra minúsculas em maiúsculas._**

---
```python
nome = input('Digite uma palavra: ')

nome = nome[::-1]

print(nome.upper())
```
---

### **Questão 7:**
 **Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de
escada, usando apenas letras maiúsculas. Por exemplo:**
 - **Entrada:**
```
Nome = Vanessa
```
 - **Saída:**
```
V
VA
VAN
...
```

### **Resolução:**
> **_Usaremos um slice que retornara a string até o index "i" do loop._**

---
```python
plv = input('Digite uma palavra: ').upper()

for i in range(len(plv) + 1):
    print(plv[:i])
```
---

### **Questão 8:**
 **Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa e
imprima a data com o mês escrito por extenso. Por exemplo:**
 - **Entrada:**

```
Data = 20/02/1995
```
> - **_Saída:_**
```
20 de fevereiro de 1995
```

### **Resolução:**

> **_Usaremos a função `split('/')` que retornara o dia, mes e ano recebidos no input
> separadamente. Depois imprimimos uma string com a data por extenso com a ajuda 
> de uma lista contendo o nome de todos os meses._**

---
```python
dia, mes, ano = input('Insira uma data (ex.: dd/mm/aaaa): ').split('/')

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
         'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print(f'{dia} de {meses[int(mes)-1]} de {ano}')
```
---
