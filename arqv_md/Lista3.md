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

 **Faça um programa para listar todos os divisores de um número ou dizer que o número
 é primo caso não existam divisores. Ao final, verifique se o usuário deseja analisar
 outro número.**

### **Resolução:**

> **_Sabendo que os unicos divisores de um número primo são 1 e ele mesmo, a lógica da questão
>  é simplesmente contar o número de divisores: dado um valor de entrada, estabelecemos a
>  variavel "count" como contador e iniciamos um `for` que vai desde o número inserido até o numero 1
>  (inverter o `for` é opcional) e tentamos dividir o valor da entrada pelos numeros gerados; se o resto 
>  da divisão for zero, então o número é um divisor: acrescentamos 1 ao "count" e exibimos a
>  operação. Se ao final o valor de entrada obtiver apenas dois divisores então, certamente, ele é
>  um número primo._**

---
```python
res = ''
while res != 'n':
    num = int(input('Digite um número: '))

    count = 0
    for div in range(num, 0, -1):
        if num % div == 0:
            count += 1
            print(f'{num}/{div} = {num/div}')
    if num_div == 2:
        print('O numero é primo.')
    
    res = input('Deseja analisar outro numero? (S/N)').lower()
```
---

### **Questão 5:**

 **Faça um programa que calcule o retorno de um investimento financeiro fazendo as
 contas mês a mês.**
 - **O usuário deve informar quanto será investido por mês e qual será a taxa de
 juros mensal;**
 - **O programa deve informar o saldo do investimento após um ano (soma das
 aplicações mês a mês considerando os juros compostos), e perguntar ao
 usuário se ele deseja que seja calculado o ano seguinte, sucessivamente;**
 - **Por exemplo, caso o usuário deseje investir R$ 100,00 por mês, e tenha uma
 taxa de juros de 1% ao mês, o programa forneceria a seguinte saída:**

```
Saldo do investimento após 1 ano: R$ 1268.25 Deseja processar mais um ano? (S/N)
```

### **Resolução:**

> **_Para deixar o código mais prático, definimos a função `calcularJuros()` que recebe como parâmetros
> o valor de investimento, de juros e saldo, e retorna o saldo do investimento após 12 meses (calculado
> a partir da fórmula do juros compostos). Ademais, o valor é informado ao usuário e ele pode, se desejar,
> calcular o valor de mais anos._**

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
ano = 1

saldo = calcularJuros(inves, juros, saldo)
res = input(f'\nSaldo do investimento após {ano} ano: R${saldo}\nDeseja processar mais um ano?(S/N)\n').lower()
while res != 'n':
    saldo = calcularJuros(inves, juros, saldo)
    ano += 1
    res = input(f'\nSaldo do investimento após {ano} anos: R${saldo}\nDeseja processar mais um ano?(S/N)\n').lower()
```
---

### **Questão 6:**
 **Escreva um programa que imprime na tela os n primeiros números perfeitos. Um
 número perfeito é aquele que é igual à soma dos seus divisores. Por exemplo, 6 = 1 +
 2 + 3.**

### **Resolução:**

> **_Definimos a função `numPerfeito()` que recebe o valor de entrada como parâmetro: estabelecemos
> "divisores" para guardar todos os números cujo o valor é divisível por (para todos os valores de 
> 1 á n, se o resto da divisão de n por ele for zero, então o número é um divisor de n). Por fim, se
> a soma de todos os elementos da lista de divisores for igual ao valor de entrada, a função retornará
> `True`, caso contrário retornará `False`._**

---
```python
def numPerfeito(n):
    divisores = list()
    for val in range(1, n):
        if n % val == 0:
            divisores.append(val)
    if sum(divisores) == n:
        return True
    else:
        return False


n = int(input('Exibir perfeitos até o número: '))

for val in range(1, n + 1):
    if (numPerfeito(val)):
        print(val)
```
---

### **Questão 7:**
 **Um número inteiro pode ser igual ao produto de 3 números inteiros consecutivos,
como, por exemplo, 120 = 4 x 5 x 6. Elabore um programa que, após ler um número n
do teclado, verifique se n tem essa propriedade.**

### **Resolução:**

> **_A idéia do programa é bem simples: dado um determinado valor de entrada, realizamos
> um `for` que vai de 1 até o valor inserido; para cada número, é verificado se seu produto
> com seus dois numeros consecutivos é igual ao valor inserido; se sim, então guardamos o número
> na variável "num", antes iniciada com o valor zero. Por fim, verificamos se o valor da variável
> "num" foi alterado. Se sim, o valor satisfaz a condição dentro do `for`._**

---
```python
valor = int(input('Digite um número: '))

num = 0
for i in range(1, valor):
    if i * (i+1) * (i+2) == valor:
        num = i   

if num != 0:
    print(f'{valor} é o produto de {num} x {num+1} x {num+2}')
else:
    print(f'{valor} não é produto de inteiros consecutivos.')
```
---

### **Questão 8:**
 **Elabore um programa que leia n valores e mostre a soma de seus quadrados.**

### **Resolução:**

> **_Simples: adicionamos o valor de input já elevado ao quadrado no vetor e ao
> final somamos os valores do vetor usando a função `sum()`._**

---
```python
vetor = list()
res = ''
while res != 'n':
    vetor.append(int(input('Digite o valor: '))**2)
    res = input('Deseja inserir mais um valor? (S/N)').lower()
print(sum(vetor))
```
---

### **Questão 9:**
 **Faça um programa que leia dois valores x e y, e calcula o valor de x dividido por y,
além do resto da divisão. Não é permitido usar as operações de divisão e resto de
divisão do Python (use apenas soma e subtração).**

### **Resolução:**

> **_Essa é um pouco complicada: recebemos valores inteiros para o dividendo e o divisor. Iniciamos a variável
> "resultado" - que indicará quantas vezes conseguimos dividir o valor - com valor zero e uma outra 
> variável auxiliar "aux" para guardar o valor original do divisor. Enquanto o divisor for menor ou 
> igual ao dividendo; subtraímos o valor guardado em "aux" pelo dividendo, e guardamos o resultado 
> disso na variável "resta_dividir"; adicionamos 1 ao resultado; o valor do dividendo passa a ser o de
> "resta_dividir" - o que resta da subtração._**

---
```python
dividendo = int(input('Dividendo: '))
divisor = int(input('Divisor: '))
resultado = 0
aux = divisor
while divisor <= dividendo:
    resta_dividir = dividendo - aux
    resultado += 1
    dividendo = resta_dividir
print(f'Resultado: {resultado}\nResto: {dividendo}')
```
---

### **Questão 10:**
 **Faça um programa em Python que calcule o valor de Pi, utilizando a fórmula de
 Leibniz π/4 = 1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + 1/13 - ...**

### **Resolução:**

> **_Dado o padrão observado, de que todos os divisores das parcelas são ímpares e de que os valores em
posição par são positivos e em posição ímpar são negativos (levando em conta a notação de index do python), 
a idéia para o programa foi: executar um `for` de 1 á 1 milhão com incremento 2, cada valor dividindo 1, e
guardando todos em um vetor. Depois, percorremos o vetor e identificamos quais os valores com index
par e quais os valores com index impar, somando-os em seus respectivas variáveis acumulativas. Por fim,
o valor de pi foi obtido ao subtrair os valores em posição ímpar pelos valores em posição par e multiplicando
o resultado por 4._**

---
```python
vetor = list()
posipar = 0
posimpar = 0

#  Calculando o valor de cada fração
for i in range(1, 1000000, 2):
    inter = 1/i
    vetor.append(inter)

for j in range(len(vetor)):
    if j % 2 == 0:  # Somando os valores em posição par
        posipar += vetor[j]
    else:  # Somando os valores em posição ímpar
        posimpar += vetor[j]

pi = (posipar - posimpar)*4
print(pi)
```
---



