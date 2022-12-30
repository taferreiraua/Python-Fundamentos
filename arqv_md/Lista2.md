# Operadores e Estruturas de Decisão

### **Questão 1:**
 **Faça um programa que calcule o IMC de uma pessoa (IMC = massa em kg / altura em metros elevado ao quadrado) e 
 informe a sua classificação segundo a tabela a seguir, obtida na Wikipedia.**
 |     IMC     |         Classificação        |
 |-------------|------------------------------|
 |    <18,5    |        Abaixo do peso        |
 | 18,6 - 24,9 |           Saudável           |
 | 25,0 - 29,9 |        Peso em excesso       |
 | 30,0 - 34,9 |       Obesidade Grau I       |
 | 35,0 - 39,9 |  Obesidade Grau II (severa)  |
 |    >=40,0   | Obesidade Grau III (mórbida) |

### **Resolução:**

> **_As duas entradas foram convertidas para o tipo float. É calculado o IMC utilizando operadores basicos,
> e depois uma estrutura de decisão if/else indica a classificação._**

---
```python
peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso/(altura)**2

print(f'IMC = {imc}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.6 < imc < 24.9:
    print('Saudável')
elif 25.0 < imc < 29.9:
    print('Peso em excesso')
elif 30.0 < imc < 34.9:
    print('Obesidade Grau I')
elif 35.0 < imc < 39.9:
    print('Obesidade Grau II (severa)')
else:
    print('Obesidade Grau III (mórbida)')
```
---

### **Questão 2:**

 **Faça um programa que leia três coordenadas num espaço 2D e indique se formam um
triângulo, juntamente com o seu tipo (equilátero, isósceles e escaleno).**
- **Equilátero: todos os lados iguais;**
- **Isósceles: dois lados iguais;**
- **Escaleno: todos os lados diferentes.**

### **Resolução:**

> **_Inserida as três medidas dos lados do triângulo, uma estrutura de decisão if/else
> indica o tipo do triângulo. Para definir se as medidas configuram ou não um triângulo,
> foi tomada a noção básica de geometria de que em qualquer triângulo, cada lado é 
> menor que a soma dos outros dois lados._**

---
```python
print('Informe as medidas do triangulo\n')
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1: # Em qualquer triângulo, cada lado é menor que a soma dos outros dois lados
    print('Não é um triângulo.')
elif l1 == l2 == l3:
    print('É um equilátero.')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('É um isosceles.')
else:
    print('É um escaleno.')
```
---

### **Questão 3:**

 **Faça um programa que leia um número inteiro de 5 dígitos e indique se ele é
 palíndromo. Um número palíndromo é aquele que se lido da esquerda para a direita
 ou da direita para a esquerda possui o mesmo valor (ex.: 15451).**

### **Resolução:**

> **_A variável "numero" tem como entrada um número inteiro, e em seguida é redefinida como uma string. 
> Para verificar se o número é um palíndromo, a string foi invertida utilizando um _slice_ que se move de trás pra frente._**

---
```python
numero = int(input('Digite um número: '))

numero = str(numero)

if numero == numero[::-1]:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')
```
---
