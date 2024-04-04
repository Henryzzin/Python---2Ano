sexo=int(input("Digite 1 se for menina e 0 se for menino: "))
idade=float(input("Digite a idade: "))
if sexo==1:
    if idade<12:
        print("É uma menina")
    elif idade>=12 and idade<=24:
        print("É uma moça")
    elif idade>24:
        print("É uma mulher")
else:
    if idade<12:
        print("É um menino")
    elif idade>=12 and idade<=24:
        print("É um rapaz")
    elif idade>24:
        print("É um homem")