import numpy as np
np.set_printoptions(legacy='1.25')

m=3
matriz = np.zeros((m,m))
vetor= []
for x in range(m):
    vetor.append(float(input("Digite um valor para o vetor: ")))
print(vetor)
for i in range(m):
    for h in range(m):
        matriz[i][h]=float(input("Digite um valor para a matriz: "))
print(matriz)
matriz[0][0]=matriz[0][0]*vetor[0]
matriz[1][0]=matriz[0][1]*vetor[0]
matriz[2][0]=matriz[0][2]*vetor[0]
matriz[0][1]=matriz[1][0]*vetor[1]
matriz[1][1]=matriz[1][1]*vetor[1]
matriz[2][1]=matriz[1][2]*vetor[1]
matriz[0][2]=matriz[2][0]*vetor[2]
matriz[1][2]=matriz[2][1]*vetor[2]
matriz[2][2]=matriz[2][2]*vetor[2]
print(matriz)
