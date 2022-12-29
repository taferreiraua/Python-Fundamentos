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
    res = input('Deseja inserir outra nota? (S/N)')

media = mean(notas)
status = status(media)
print(status)
```
---

### **Questão 3:**
> **__**

---
```python

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
