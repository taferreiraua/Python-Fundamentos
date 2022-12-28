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

### **Questão 4:**

> **_Faça um programa para listar todos os divisores de um número ou dizer que o número
> é primo caso não existam divisores. Ao final, verifique se o usuário deseja analisar
> outro número._**

---
```python
num = int(input('Digite um número: '))
ndiv = 0

for div in range(num, 0, -1):
    if num % div == 0:
        res = round(num / div)
        ndiv = ndiv + 1
        print(f'{num}/{div} = {res}')
if ndiv == 2:
    print('O numero é primo.')
```
---

### **Questão 4:**

> **_Faça um programa que calcule o retorno de um investimento financeiro fazendo as
> contas mês a mês, sem usar a fórmula de juros compostos._**
> - **_O usuário deve informar quanto será investido por mês e qual será a taxa de
> juros mensal;_**
> - **_O programa deve informar o saldo do investimento após um ano (soma das
> aplicações mês a mês considerando os juros compostos), e perguntar ao
> usuário se ele deseja que seja calculado o ano seguinte, sucessivamente;_**
> - **_Por exemplo, caso o usuário deseje investir R$ 100,00 por mês, e tenha uma
> taxa de juros de 1% ao mês, o programa forneceria a seguinte saída:_**
```
Saldo do investimento após 1 ano: R$ 1268.25 Deseja processar mais um ano? (S/N)
```
---
```python
def calcularJuros(inves, juros, saldo):
    mes = 1
    while mes <= 12:
        saldo = round(saldo + (saldo * (juros / 100)) + inves, 2)
        mes = mes + 1
    return round(saldo, 2)


inves = float(input('Investimento mensal: '))
juros = float(input('Juros: '))
saldo = 0

saldo = calcularJuros(inves, juros, saldo)
ano = 1
res = input(f'\nSaldo do investimento após {ano} ano: R${saldo}\nDeseja processar mais um ano?(S/N)\n')
while res.lower() == 's':
    saldo = calcularJuros(inves, juros, saldo)
    ano += 1
    res = input(f'\nSaldo do investimento após {ano} anos: R${saldo}\nDeseja processar mais um ano?(S/N)\n')
```
---

### **Questão 6:**
> **_Escreva um programa que imprime na tela os n primeiros números perfeitos. Um
> número perfeito é aquele que é igual à soma dos seus divisores. Por exemplo, 6 = 1 +
> 2 + 3._**

---
```python
def perfeito(n):
    soma = 0
    for val in range(1, n):
        if n % val == 0:
            soma += val
    if soma == n:
        return True
    else:
        return False


n = int(input('Exibir perfeitos até o número: '))

for val in range(1, n + 1):
    if (perfeito(val)):
        print(val)
```
---

### **Questão 7:**
> **_Um número inteiro pode ser igual ao produto de 3 números inteiros consecutivos,
como, por exemplo, 120 = 4 x 5 x 6. Elabore um programa que, após ler um número n
do teclado, verifique se n tem essa propriedade._**

---
```python
num = int(input('Digite um número: '))
i = 1
while i * (i+1) * (i+2) < num:
    i = i + 1
if i * (i+1) * (i+2) == num:
    print(f'{num} é o produto de {i} x {i+1} x {i+2}')
else:
    print(f'{num} não é produto de inteiros consecutivos.')
```
---

### **Questão 8:**
> **_Elabore um programa que leia n valores e mostre a soma de seus quadrados._**

---
```python

```
---
