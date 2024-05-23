inferior=int(input("Qual o limite inferior do intervalo? "))
superior=int(input("Qual o limite superior do intervalo? "))

for num in range(inferior, superior+1):
    if num%2==0:
        print(num)