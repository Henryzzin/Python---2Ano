import numpy as np
N=3
soma=0
matriz = np.zeros((N,N))

for x in range (0,2):
    for i in range (0,2):
        matriz[x][i]=input("Digite valores para a matriz: ")
print(matriz)
for x in range (0,2):
    for i in (0,2):
        soma+=matriz[x][i]
print(soma)