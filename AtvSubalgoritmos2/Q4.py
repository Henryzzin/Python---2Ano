def calculadora(n1,n2):
    opcao=int(input("Digite 1 para adição, 2 para subtração, 3 para divisão e 4 para multiplicação entre os números."))
    if(opcao==1):
        total=n1+n2
    elif(opcao==2):
        total=n1-n2
    elif(opcao==3):
        total=n1/n2
    elif(opcao==4):
        total=n1*n2
    else:
        print('Nenhuma opção digitada.')
        return
    return total
total=0
n1=int(input("Digite um número: "))
n2=int(input("Digite um número: "))
total=calculadora(n1,n2)
print(total)
