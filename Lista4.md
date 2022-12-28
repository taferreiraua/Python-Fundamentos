# Manipulação de Strings em Python

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
```
---

### **Questão 3:**
> **_Faça um programa que recebe uma frase e substitui todas as ocorrências de espaço por
“#”._**

---
```python
```
---

### **Questão 4:**
> **_Faça um programa que decida se duas strings lidas do teclado são palíndromas
mútuas, ou seja, se uma é igual à outra quando lida de trás para frente. Exemplo:
amor e roma._**

---
```python
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
```
---

### **Questão 6:**
> **_Faça um programa que leia o nome do usuário e mostre o nome de trás para frente,
utilizando somente letras maiúsculas. Exemplo: Nome = Vanessa. Resultado gerado
pelo programa: ASSENAV._**

---
```python
```
---

### **Questão 7:**
> **_Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de
escada, usando apenas letras maiúsculas. Por exemplo:
<br/>   Entrada:_**
```
Nome = Vanessa
```
> **_   Saída:_**
```python
V
VA
VAN
...
```

---
```python
```
---

### **Questão 8:**
> **__**

---
```python
```
---
