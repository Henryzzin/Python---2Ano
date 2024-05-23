Maior=0
menor= 100000000000000
for num in range(1,11):
    a=int(input("Digite um número:"))
    if a>Maior:
        Maior=a
    if a<menor:
        menor=a
print("Menor:", menor)
print("Maior:", Maior)
        