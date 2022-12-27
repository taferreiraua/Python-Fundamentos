# Operadores e Estruturas de Decisão

### **Questão 1:**
> **_Faça um programa que calcule o IMC de uma pessoa (IMC = massa em kg / altura em metros elevado ao quadrado) e 
> informe a sua classificação segundo a tabela a seguir, obtida na Wikipedia._**
> |     IMC     |         Classificação        |
> |-------------|------------------------------|
> |    <18,5    |        Abaixo do peso        |
> | 18,6 - 24,9 |           Saudável           |
> | 25,0 - 29,9 |        Peso em excesso       |
> | 30,0 - 34,9 |       Obesidade Grau I       |
> | 35,0 - 39,9 |  Obesidade Grau II (severa)  |
> |    >=40,0   | Obesidade Grau III (mórbida) |

---
```python
peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso/(altura)**2

print(f'IMC = {imc}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.6 < imc < 24.9:
    print('Saudável')
elif 25.0 < imc < 29.9:
    print('Peso em excesso')
elif 30.0 < imc < 34.9:
    print('Obesidade Grau I')
elif 35.0 < imc < 39.9:
    print('Obesidade Grau II (severa)')
else:
    print('Obesidade Grau III (mórbida)')
```
---

### **Questão 2:**

