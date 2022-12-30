# Manipulação de Strings

### **Questão 1:**
> **_Escreva um programa que lê uma frase, uma palavra antiga e uma palavra nova. O
programa deve imprimir a frase com as ocorrências da palavra antiga substituídas pela
palavra nova. Por exemplo:_**
> - **_Frase: “Quem parte e reparte fica com a maior parte”_**
> - **_Palavra antiga: “parte”_**
> - **_Palavra nova: “parcela”_**
> - **_Saída: “Quem parcela e reparte fica com a maior parcela”_**

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
> **_Faça um programa que lê uma frase e retorna o número de palavras que a frase
contém. Considere que a palavra pode começar e/ou terminar por espaços._**

---
```python
frase = input('Digite a frase: ')

plv = frase.split()

print(f'Há {len(plv)} palavras nesta frase.')
```
---

### **Questão 3:**
> **_Faça um programa que recebe uma frase e substitui todas as ocorrências de espaço por
“#”._**

---
```python
frase = input('Digite uma frase: ')

print(frase.replace(' ', '#'))
```
---

### **Questão 4:**
> **_Faça um programa que decida se duas strings lidas do teclado são palíndromas
mútuas, ou seja, se uma é igual à outra quando lida de trás para frente. Exemplo:
amor e roma._**

---
```python
plv = input('Digite uma palavra: ')

vlp = plv[::-1]
if plv == vlp:
    print('A palavra é um palindromo.')
else:
    print('Não é um palindromo.')
```
---

### **Questão 5:**
> **_Um anagrama é uma palavra que é feita a partir da transposição das letras de outra
palavra ou frase. Por exemplo, “Iracema” é um anagrama para “America”. Escreva
um programa que decida se uma string é um anagrama de outra string, ignorando os
espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo
caracteres iguais, ou seja, “a” = “A”._**

---
```python
def isanagrama(plv1: str, plv2: str):
    if len(plv1) != len(plv2):
        return False
    else:
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
> **_Faça um programa que leia o nome do usuário e mostre o nome de trás para frente,
utilizando somente letras maiúsculas. Exemplo: Nome = Vanessa. Resultado gerado
pelo programa: ASSENAV._**

---
```python
nome = input('Digite uma palavra: ')

nome = nome[::-1]

print(nome.upper())
```
---

### **Questão 7:**
> **_Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de
escada, usando apenas letras maiúsculas. Por exemplo:_**
> - **_Entrada:_**
```
Nome = Vanessa
```
> - **_Saída:_**
```
V
VA
VAN
...
```

---
```python
plv = input('Digite uma palavra: ').upper()

for i in range(len(plv) + 1):
    print(plv[:i])
```
---

### **Questão 8:**
> **_Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa e
imprima a data com o mês escrito por extenso. Por exemplo:_**
> - **_Entrada:_**
```
Data = 20/02/1995
```
> - **_Saída:_**
```
20 de fevereiro de 1995
```

---
```python
dia, mes, ano = input('Insira uma data (ex.: dd/mm/aaaa): ').split('/')

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
         'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print(f'{dia} de {meses[int(mes)-1]} de {ano}')
```
---
