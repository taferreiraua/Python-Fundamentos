# Estruturas de Repetição em Python

### **Questão 1:**

> **_Faça um programa para montar a tabela de multiplicação de números de 1 a 10
> (exemplo: 1 x 1 = 1, 1 x 2 = 2...)._**

---
```python
num = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{num}x{i}={i*num}')
```
---
