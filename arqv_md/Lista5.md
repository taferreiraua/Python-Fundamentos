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

> **_Definimos a função `MenorDesvio` que recebe o vetor como parâmetro e: calcula a media,
> constroi um dicionario com cada valor do vetor e a diferença entre ele e a media. Ao fim,
> a função retorna o valor que obteve a menor diferença._**

---
```python
from numpy import mean


def MenorDesvio(vetor):
    media = mean(vetor)
    valores = dict()
    for num in vetor:
        valores[num] = abs(num - media)
    return min(valores, key=valores.get)


res = ''
vetor = list()
while res != 'n':
    vetor.append(float(input('Digite um número: ')))
    res = input('Deseja adicionar mais um número? (S/N)').lower()

print(f'Numero mais proximo da media: {MenorDesvio(vetor)}')
```
---

### **Questão 3:**
 **Faça um programa que percorre duas listas e intercala os elementos de ambas,
formando uma terceira lista. A terceira lista deve começar pelo primeiro elemento da
lista menor.**

### **Resolução:**

> **_Definimos a função `dimLista()`, que retornará qual a menor e a maior lista. Para unir
> as listas, definimos `intercalarListas()`: primeiro usamos o `zip()`, que vai unir os valores 
> de cada lista em tuplas, e adicionamos os valores em um terceiro vetor. Para adicionar os valores
> restantes (observe que agora todos os valores da lista menor já foram adicionados), dividiremos
> o tamanho da lista intercalada por 2, e usaremos esse valor como índice. Então, usaremos um slice
> que vai desde o índice calculado até o final da lista maior._**

---
```python
def preencherVetor():
    res = ''
    vetor = list()
    while res != 'n':
        vetor.append(input('Digite um valor: '))
        res = input('Deseja inserir mais um ítem? (S/N)').lower()
    return vetor


def dimLista(vetor1, vetor2):
    menor = min(vetor1, vetor2, key=len)
    maior = max(vetor1, vetor2, key=len)
    return menor, maior


def intercalarLista(menor, maior):
    inter = list()
    for a, b in zip(menor, maior):
        inter.extend([a, b])
    indice = int(len(inter)/2)
    inter.extend(maior[indice:])
    return inter
    


vetor1 = preencherVetor()
vetor2 = preencherVetor()

menor, maior = dimLista(vetor1, vetor2)

vetor3 = intercalarLista(menor, maior)

print(f'Lista intercalada: {vetor3}')
```
---
