# Manipulação de Vetores

### **Questão 1:**
 **Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em um vetor. Depois, monte um outro vetor contendo quantas
vezes cada valor foi obtido. Imprima os dois vetores.**

### **Resolução:**

> **_Para simular o lançamento dos dados, usamos a função `random.randint()` para 
> gerar números aleatórios de 1 a 6, armazenando os resultados em uma lista. Em seguida,
> usamos a função `count()` para contar a ocorrencia de cada numero e armazenamos em outra lista._**

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
 **Faça um programa que percorre um vetor e imprime na tela a média dos valores do
vetor e o valor mais próximo da média.**

### **Resolução:**

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
 **Faça um programa que percorre duas listas e intercala os elementos de ambas,
formando uma terceira lista. A terceira lista deve começar pelo primeiro elemento da
lista menor.**

### **Resolução:**

> **__**

---
```python
def preencherVetor():
    res = ''
    vetor = list()
    while res != 'n':
        vetor.append(input('Digite um valor: '))
        res = input('Deseja inserir mais um ítem? (S/N)').lower()
    return vetor


vetor1 = preencherVetor()
vetor2 = preencherVetor()

inter = list()
for a, b in zip(vetor1, vetor2):
    inter.extend([a, b])

print(f'Lista intercalada: {inter + vetor1[len(vetor2):] + vetor2[len(vetor1):]}')
```
---
