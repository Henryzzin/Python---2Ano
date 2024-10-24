import numpy as np
def subrotina(matriz,somatotal):
    for i in range (x):
        for j in range(x):
            somatotal=somatotal+matriz[i][j]
    return somatotal
somatotal=0
x=5
matriz=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
somatotal=subrotina(matriz,somatotal)
print(somatotal)