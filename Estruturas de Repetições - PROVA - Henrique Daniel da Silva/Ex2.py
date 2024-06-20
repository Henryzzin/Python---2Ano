x=0
while x!='sair':
    y=int(input("Digite qual operação você deseja fazer:\n1)Adição\n2)Subtração\n3)Multiplicação\n4)Divisão\n5)Potenciação"))
    if y==1:
        num1=float(input("Digite o primeiro número da operação: "))
        num2=float(input("Digite o segundo número da operação: "))
        total=num1+num2
        print("O valor dessa operação é: ", total)
    elif y==2:
        num1=float(input("Digite o primeiro número da operação: "))
        num2=float(input("Digite o segundo número da operação: "))
        total=num1-num2
        print("O valor dessa operação é: ", total)
    elif y==3:
        num1=float(input("Digite o primeiro número da operação: "))
        num2=float(input("Digite o segundo número da operação: "))
        total=num1*num2
        print("O valor dessa operação é: ", total)
    elif y==4:
        num1=float(input("Digite o primeiro número da operação: "))
        num2=float(input("Digite o segundo número da operação: "))
        total=num1/num2
        print("O valor dessa operação é: ", total)
    elif y==5:
        num1=float(input("Digite a base da operação: "))
        num2=float(input("Digite em qual potência a base será feita: "))
        total=num1**num2
        print("O valor dessa operação é: ", total)
    x=input("Digite 'sair' caso deseje encerrar: ")