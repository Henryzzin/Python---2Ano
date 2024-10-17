base=int(input('Digite o valor do base do triângulo: '))
altura=int(input('Digite o valor do altura do triângulo: '))
def calculo(base, altura):
    area_triangulo=base*altura/2
    return area_triangulo
area=calculo(base, altura)
print("A área do quadrado é de: ",area,"metros²")