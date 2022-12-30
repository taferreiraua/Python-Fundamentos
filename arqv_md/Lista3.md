# Estruturas de Repetição em Python

### **Questão 1:**

 **Faça um programa para montar a tabela de multiplicação de números de 1 a 10
 (exemplo: 1 x 1 = 1, 1 x 2 = 2...).**

### **Resolução:**

> **_O programa recebe como entrada um numero inteiro, que é multiplicado de 1 á 10 utilizando
> uma estrutura de repetição `for` com `range(1, 11)`._**

---
```python
num = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{num}x{i}={i*num}')
```
---

### **Questão 2:**
 **Faça um programa para determinar o número de dígitos de um número inteiro
positivo informado**

### **Resolução:**

> **_O programa tem como entrada um numero inteiro, e utiliza a função `len()` para 
> determinar o número de digitos. Esta função retorna o número de itens em uma
> string, array, listas, etc., mas não funciona em objetos do tipo inteiro. Assim, a
> variavel foi convertida como str antes de ser passada para função._**

---
```python
num = int(input('Digite um número inteiro positivo: '))

print(f"O número possui {len(str(num))} digitos.")
```
---


### **Questão 3:**
 **Faça um programa para calcular a série de Fibonacci para um número informado pelo
 usuário, sendo F(0) = 0, F(1) = 1 e F(n)= F(n-1)+F(n-2). Por exemplo, caso o usuário
 informe o número 9, o resultado seria: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.**
 
### **Resolução:**

> **_A sucessão de Fibonacci é uma sequência de números inteiros iniciados por zero e um, 
> no qual cada termo subsequente corresponde a soma dos dois números anteriores. Existe uma
> discussão sobre o primeiro termo da sequencia ser 0 ou 1, então assumiremos o primeiro
> termo como 0 devido ao exemplo dado no enunciado. <br/> Assim, para os numeros 0 e 1, as 
> sequencias são "0" e "0, 1" respectivamente. Para o restante, a lógica do programa é a seguinte: 
> <br/> Definimos "fibon" como uma lista que será utilizada para guardar a sequencia do numero de entrada;
> usando a função `extend()` adicionamos á lista os números 0, 1 e 1, que são os primeiros elementos de todo
> e qualquer número maior que 1; definimos as variaveis "ultimo" e "penultimo" ambas com valor 1 -
> os dois ultimos numeros da sequencia até o momento; do número 2 até o numero inserido, fazemos o proximo número
> a soma dos dois anteriores; desse modo, "penultimo" passa a ser o valor que estava armazenado em "ultimo", e 
> "ultimo" passa a ter o valor de "prox"; por fim, adicionamos o valor de "prox" á lista._**

---
```python
num = int(input("Digite um número: "))

fibon = list()
if num == 0:
    fibon.append(0)
elif num == 1:
    fibon.extend([0, 1])
else:
    fibon.extend([0, 1, 1])
    ultimo = 1
    penultimo = 1
    for i in range(2, num):
        prox = ultimo + penultimo
        penultimo = ultimo
        ultimo = prox
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

### **Questão 5:**

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
vet = list()
res = ''
while res != 'n':
    vet.append(int(input('Digite o valor: '))**2)
    res = input('Deseja inserir mais um valor? (S/N)').lower()
print(sum(vet))
```
---

### **Questão 9:**
> **_Faça um programa que leia dois valores x e y, e calcula o valor de x dividido por y,
além do resto da divisão. Não é permitido usar as operações de divisão e resto de
divisão do Python (use apenas soma e subtração)._**

---
```python
num = int(input('Dividendo: '))
div = int(input('Divisor: '))
res = 0
aux = div
while div <= num:
    ddiv = num - aux
    res = res + 1
    num = ddiv
print(f'Resultado: {res}\nResto: {num}')
```
---

### **Questão 10:**
> **_Faça um programa em Python que calcule o valor de Pi, utilizando a fórmula de
> Leibniz π/4 = 1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + 1/13 - ..._**

---
```python
vetor = list()
posipar = 0
posimpar = 0

#  Calculando o valor de cada fração
for i in range(1, 1000000, 2):
    inter = 1/i
    vetor.append(inter)

for j in range(500000):
    if j % 2 == 0:  # Somando os valores em posição par
        posipar += vetor[j]
    else:  # Somando os valores em posição ímpar
        posimpar += vetor[j]

pi = (posipar - posimpar)*4
print(pi)
```
---



