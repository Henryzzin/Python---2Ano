import numpy as np
par=0
impar=0
imparsoma=0
m=10
vetor= np.zeros(m)
for i in range(m):
    vetor[i]=float(input("Digite números para o array: "))
    if(vetor[i])%2==0:
        par=par+1
    else:
        imparsoma=imparsoma+vetor[i]
        impar=impar+1
print("Média dos Impares: ",imparsoma/impar)
print("Quantidade de pares: ", par)
