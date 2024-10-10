import numpy as np

m=6
matriz = np.zeros((m,m))
for i in range(m):
    for h in range(m):
        matriz[i][h]=float(input("Digite um valor para a matriz: "))
print(matriz)
for i in range(m):
    matriz[1][i]=matriz[4][i]
for i in range(m):
    matriz[i][3]=matriz[i][5]
print (matriz)