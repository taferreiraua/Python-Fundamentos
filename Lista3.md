# Estruturas de Repetição em Python

### **Questão 1:**

> **_Faça um programa para montar a tabela de multiplicação de números de 1 a 10
> (exemplo: 1 x 1 = 1, 1 x 2 = 2...)._**

---
```python
num = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{num}x{i}={i*num}')
```
---

### **Questão 2:**
> **_Faça um programa para determinar o número de dígitos de um número inteiro
positivo informado_**
---
```python
num = int(input('Digite um número inteiro positivo: '))

print(f"O número possui {len(str(num))} digitos.")
```
---


### **Questão 3:**
> **_Faça um programa para calcular a série de Fibonacci para um número informado pelo
> usuário, sendo F(0) = 0, F(1) = 1 e F(n)= F(n-1)+F(n-2). Por exemplo, caso o usuário
> informe o número 9, o resultado seria: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34._**

---
```python
num = int(input("Digite um número: "))

if num == 0:
    fibon = '[0]'
elif num == 1:
    fibon = '[0, 1]'
else:
    fibon = list()
    fibon.append(0)
    fibon.append(1)
    fibon.append(1)
    ultimo = 1
    penultimo = 1
    for i in range(2, num):
        prox = ultimo + penultimo
        penultimo = ultimo
        ultimo = prox
        i += 1
        fibon.append(prox)

print(f'A série fibonnaci para esse número é {fibon}')
```
---

###  
