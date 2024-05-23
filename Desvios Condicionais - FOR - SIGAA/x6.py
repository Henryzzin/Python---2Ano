total=0
negativos=0
for num in range(0,20):
    a=float(input("Digite um número: "))
    if a>0:
        total=total+a
    if a<0:
        negativos=negativos+1
print("A soma dos positivos é de: ",total,".\nHá um total de",negativos,"números negativos.")