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

```
---

### **Questão 3:**
> **__**

---
```python

```
---
