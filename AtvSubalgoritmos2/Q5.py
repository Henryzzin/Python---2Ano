def subrotina(matriz, somadiagonal):
    for i in range(4):
        somadiagonal=somadiagonal+matriz[i][i]
    return somadiagonal
somadiagonal=0
matriz=[[1,2,3,4],[6,7,8,9],[11,12,13,14],[16,17,18,19]]
soma=subrotina(matriz, somadiagonal)
print(soma)
