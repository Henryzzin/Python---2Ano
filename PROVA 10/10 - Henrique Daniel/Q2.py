import numpy as np

a=4
vetor = []
invertido = []
for i in range(5):
    vetor.append(float(input("Digite números para o array: ")))
print(vetor)
for i in range(5):
    invertido.append(vetor[a]*-1)
    a=a-1
print(invertido)
