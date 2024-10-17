a=int(input('Digite um valor: '))
b=int(input('Digite um valor: '))
def maior(a,b):
    if(a>b):
        print("O número ",a,"é o maior.")
    elif(a<b):
        print("O número ",b,"é o maior.")
    else:
        print("Os números são iguais.")
maior(a,b)