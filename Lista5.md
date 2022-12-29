# Manipulação de Vetores em Python

### **Questão 1:**
> **_Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em um vetor. Depois, monte um outro vetor contendo quantas
vezes cada valor foi obtido. Imprima os dois vetores. Use a função
random.randint(1,6) para gerar números aleatórios, simulando os lançamentos dos
dados._**

---
```python
import random


resultados = list()
for i in range(100):
    resultados.append(random.randint(1, 6))
print(resultados)

ocorrencias = list()
for num in range(1, 7):
    ocorrencias.append(resultados.count(num))
print(ocorrencias)
```
---

### **Questão 2:**
> **__**

---
```python
res = ''
vetor = list()
while res != 'n':
    vetor.append(int(input('Digite um número: ')))
    res = input('Deseja adicionar mais um número? (S/N)').lower()

media = sum(vetor)/len(vetor)

maiores = list()
menores = list()
for num in sorted(vetor):
    if media <= num:  # pega os valores maiores ou iguais a media
        maiores.append(num)
    if media >= num:  # pega os valores menores ou iguais a media
        menores.append(num)

proxMai = maiores[0]  # menor numero dentre os valores maiores que a media
proxMen = menores[-1]  # maior numero dentre os valores menores que a media

# Compara a diferença entre proxMai e proxMen (usando modulo)
#  1) Se existirem dois numeros igualmente proximos á media:
if abs(proxMai - media) == abs(proxMen - media) and proxMen != proxMai:
    print(f'Valores mais próximos da média: {proxMen}, {proxMai}')
#  2) Se o numero da media estiver presente no vetor:
elif proxMai == proxMen:
    print(f'Valor mais próximo da média: {proxMai}')
#  3) Se a distancia de proxMai/media for maior que a de prox3/media:
elif abs(proxMai - media) > abs(proxMen - media):
    print(f'Valor mais próximo da média: {proxMen}')
#  4) Se a distancia de prox3/media for maior que a de prox2/media:
elif abs(proxMai - media) < abs(proxMen - media):
    print(f'Valor mais próximo da média: {proxMai}')
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
