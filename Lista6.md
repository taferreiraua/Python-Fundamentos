# Funções

### **Questão 1:**
> **_O professor deseja dividir uma turma com N alunos em dois grupos: um com M
alunos e outro com (N-M) alunos. Faça o programa que lê o valor de N e M e informa
o número de combinações possíveis. Número de combinações é igual a N!/(M! * (N-M)!).
Use funções para evitar repetição de código._**

---
```python
def fatorial(num):
    fat = 1
    while num != 1:
        fat = fat * num
        num = num - 1
    return fat


def combinacao(num_m, num_n):
    n = fatorial(num_m)
    m = fatorial(num_n)
    mn = fatorial(num_m - num_n)
    comb = n / (m * mn)
    return comb


n = int(input('Total de alunos: '))
m = int(input('Digite o numero de pessoas do 1° grupo: '))

print(f'Numero de combinações: {combinacao(n, m)}')
```
---

### **Questão 2:**
> **_Faça uma função que informe o status do aluno a partir da sua média de acordo com a
tabela a seguir:_**
- **_Nota acima de 6 ⇒ “Aprovado”_**
- **_Nota entre 4 e 6 ⇒ “Verificação Suplementar”_**
- **_Nota abaixo de 4 ⇒ “Reprovado”_**

---
```python
from numpy import mean


def status(media):
    if media >= 6:
        return f'Status: Aprovado.'
    elif 4 <= media < 6:
        return f'Status: Verificação Suplementar.'
    elif media < 4:
        return f'Status: Reprovado.'


res = ''
notas = list()
while res != 'n':
    notas.append(int(input('Digite a nota: ')))
    res = input('Deseja inserir outra nota? (S/N)').lower()

media = mean(notas)
status = status(media)
print(status)
```
---

### **Questão 3:**
> **_Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções
sempre que necessário. Cada opção deve usar como operando um número lido do
teclado e o valor atual da memória. Por exemplo, se o estado atual da memória é 5, e
o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). Após a
conclusão da soma, o novo estado da memória passa a ser 8._**

---
```python
def soma(mem, n):
    sum = mem + n
    return sum


def subt(mem, n):
    sub = mem - n
    return sub


def mult(mem, n):
    mul = mem * n
    return mul


def divi(mem, n):
    div = mem / n
    return div


opc = 0
mem = 0
while opc != 6:
    print(f'Estado da memória: {mem}')
    print(f'Selecione uma opção:')
    print(f'[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir\n[5] Limpar memória\n[6] Sair do programa')
    opc = int(input(f'------> '))
    if 0 < opc < 5:
        n = float(input(f'Digite o valor: '))
        if opc == 1:
            mem = soma(mem, n)
        elif opc == 2:
            mem = subt(mem, n)
        elif opc == 3:
            mem = mult(mem, n)
        elif opc == 4:
            mem = divi(mem, n)
    elif opc == 5:
        mem = 0
    elif opc == 6:
        break
    else:
        print(f'\nSELECIONE UMA OPÇÃO VÁLIDA!\n')
```
---

### **Questão 4:**
> **__**

---
```python

```
---

### **Questão 5:**
> **__**

---
```python

```
---
