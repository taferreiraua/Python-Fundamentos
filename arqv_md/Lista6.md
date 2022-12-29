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


if __name__ == '__main__':
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


if __name__ == '__main__':
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
def somar(mem, n):
    return mem + n


def subtrair(mem, n):
    return mem - n


def multiplicar(mem, n):
    return mem * n


def dividir(mem, n):
    return mem / n


def limpar_memoria():
    return 0.0


def encerrar():
    print('Encerrando...')


def calculadora(mem, opc, n):
    menu = {1: somar(mem, n),
            2: subtrair(mem, n),
            3: multiplicar(mem, n),
            4: dividir(mem, n),
            5: limpar_memoria(),
            6: encerrar()}
    if 1 <= opc <= 6:
        mem = menu[opc]
    else:
        print(f'\nSELECIONE UMA OPÇÃO VÁLIDA!\n')

    return mem


if __name__ == '__main__':
    mem = 0.0
    n = 1
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
        mem = calculadora(mem, opc, n)
```
---

### **Questão 4:**
> **_Faça um programa que, dado uma figura geométrica que pode ser uma circunferência,
triângulo ou retângulo, calcule a área e o perímetro da figura. O programa deve primeiro 
perguntar qual o tipo da figura: circunferência, triângulo ou retângulo. Dependendo do 
tipo de figura, ler o (1) tamanho do raio da circunferência; (2) tamanho de cada um dos 
lados do triângulo; (3) tamanho dos dois lados retângulo. Usar funções sempre que possível._**

---
```python
from math import sqrt


def circunferencia(raio):
    peri = round(2 * 3.14 * raio, 2)
    area = round(3.14 * raio * raio, 2)
    return f'Area = {area}\nPerimetro = {peri}'


def triang_isosceles(l1, l2, base):
    peri = round(l1 + l2 + base, 2)
    area = round(base * ((l1*l1) - (l2*l2 / 4)) / 2, 2)
    return f'Area = {area}\nPerimetro = {peri}'


def triang_escaleno(l1, l2, l3):
    peri = round(l1 + l2 + l3/3, 2)
    area = round(sqrt(peri*(peri - l1)*(peri - l2)*(peri - l3)), 2)
    return f'Area = {area}\nPerimetro = {peri}'


def triang_equilatero(l1, l2, l3):
    peri = round(l1 + l2 + l3, 2)
    area = round(l1*l1*sqrt(3)/4, 2)
    return f'Area = {area}\nPerimetro = {peri}'


def retangulo(base, altu):
    peri = round(base * altu, 2)
    area = round(2 * (base + altu), 2)
    return f'Area = {area}\nPerimetro = {peri}'


if __name__ == '__main__':
    opc = 1
    while opc != 0:
        opc = int(input(f'Figura:\n[1] Circunferencia\n[2] Triângulo\n[3] Retângulo\nDigite 0 para sair-----> '))
        if opc == 1:
            print(circunferencia(float(input('Raio: '))))
        elif opc == 2:
            res = int(input('Informe o tipo do triâgulo:\n[1] Isosceles\n[2] Escaleno\n[3] Equilátero\n\t-----> '))
            l1 = float(input('Lado 1: '))
            l2 = float(input('Lado 2: '))
            l3 = float(input('Lado 3: '))
            menu = {1: triang_isosceles(l1, l2, l3),
                    2: triang_escaleno(l1, l2, l3),
                    3: triang_equilatero(l1, l2, l3)}
            print(menu[res])
        elif opc == 3:
            print(retangulo(float(input('Base: ')), float(input('Altura: '))))
        elif opc > 3 or opc < 0:
            print('\nDIGITE UMA OPÇÃO VÁLIDA!')
```
---
