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
> - **_Nota acima de 6 ⇒ “Aprovado”_**
> - **_Nota entre 4 e 6 ⇒ “Verificação Suplementar”_**
> - **_Nota abaixo de 4 ⇒ “Reprovado”_**

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
    return mem + n


def subt(mem, n):
    return mem - n


def mult(mem, n):
    return mem * n


def divi(mem, n):
    return mem / n


def limpar_mem():
    return 0.0


def calculadora(mem, opc):
    if 1 <= opc <= 6:
        menu = {1: soma(mem, n),
                2: subt(mem, n),
                3: mult(mem, n),
                4: divi(mem, n),
                5: limpar_mem(),
                6: print('Encerrando...')}
        mem = menu[opc]
    else:
        print(f'\nSELECIONE UMA OPÇÃO VÁLIDA!\n')

    return mem


mem = 0.0
opc = 0
while opc != 6:
    print(f'Estado da memória: {mem}\n'
              f'Selecione uma opção:\n'
              f'[1] Somar\n'
              f'[2] Subtrair\n'
              f'[3] Multiplicar\n'
              f'[4] Dividir\n'
              f'[5] Limpar memória\n'
              f'[6] Sair do programa')
    opc = int(input(f'------> '))
    if 1 <= opc <= 4:
        n = float(input(f'Digite o valor: '))
    mem = calculadora(mem, opc)
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
