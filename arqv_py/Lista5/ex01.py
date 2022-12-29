import random


resultados = list()
for i in range(100):
    resultados.append(random.randint(1, 6))
print(resultados)

ocorrencias = list()
for num in range(1, 7):
    ocorrencias.append(resultados.count(num))
print(ocorrencias)
