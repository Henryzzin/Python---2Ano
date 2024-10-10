import numpy as np
np.set_printoptions(legacy='1.25')

p=0
n=0
m=8
vetor= np.zeros(m)
positivo= {}
negativo= {}
for i in range(m):
    vetor[i]=float(input("Digite números para o array: "))
    if vetor[i]>0:
        positivo[p]=vetor[i]
        p+=1
    elif vetor[i]<0:
        negativo[n]=vetor[i]
        n+=1
print(vetor)
print(positivo)
print(negativo)
