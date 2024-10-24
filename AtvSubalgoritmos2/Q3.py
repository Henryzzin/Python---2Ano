import numpy as np
vetor= np.zeros(15)
def subrotina(vetor):
    for i in range (15):
        if(vetor[i]<0):
            vetor[i]=0
    return vetor
for i in range(15):
    if(i%2!=0):
        vetor[i]=i-30
    else:
        vetor[i]=i
vetornovo=subrotina(vetor)
print(vetornovo)