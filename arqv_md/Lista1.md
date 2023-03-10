# Organização de Programas em Python

### **Questão 1:**

 **Faça um programa que leia o nome, a idade, a altura, o peso e a nacionalidade do usuário 
 e escreva essas informações na forma de um parágrafo de apresentação.**

### **Resolução:**

> **_As variáveis "nome" e "nacionalidade" são do tipo string - padrão do `input()`, "altura" 
> e "peso" do tipo float e "idade" do tipo int. Para exibir a string de informações, foi utilizada 
> a função `print()`, com a string formatada em `'f'` para concatenar as strings com os valores das variáveis._**

---
```python
nome = input('Nome: ')
idade = int(input('Idade: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))
nacionalidade = input('Nacionalidade: ')

print(f'\nInformações do usuário:\n'
      f'Nome: {nome}\n'
      f'Idade: {idade}\n'
      f'Altura: {altura}\n'
      f'Peso: {peso}\n'
      f'Nacionalidade: {nacionalidade}')
```
---

### **Questão 2:**

 **Faça um programa que exiba o perímetro de uma circunferência a partir do seu raio.**
 
### **Resolução:**

> **_A entrada foi formatada para o tipo float, e para calcular o perímetro, além dos operadores
> básicos, foi utilizado a constante `pi` da biblioteca `math`._**
 
---
```python
from math import pi


raio = float(input('Raio: '))
print(f'Perímetro: {2*pi*raio}')
```

### **Questão 3:**

 **Faça um programa que leia dois pontos num espaço bidimensional e calcule a distância entre esses pontos.**

### **Resolução:**

> **_Todas as entradas correspondentes as coordenadas foram convertidas para float, e para calcular a distância
> foi utilizada a função `sqrt()` da biblioteca `math`._**

---
```python
from math import sqrt


x1 = float(input('Ponto 1: \n'
                 'x1: '))
y1 = float(input('y2: '))
x2 = float(input('Ponto 2: \n'
                 'x2: '))
y2 = float(input('y2: '))

distancia = sqrt((x2-x1)**2 + (y2-y1)**2)

print(f'A distância entre os dois pontos é {distancia}')
```

---
