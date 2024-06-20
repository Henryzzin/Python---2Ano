x=1
total=0
cont=0
while x>0:
    x=float(input("Digite um número, caso deseje parar, digite um número negativo: "))
    if x>0:
        total=total+x
        cont=cont+1        
media=total/cont
print("A média dos números digitados é: ", media)