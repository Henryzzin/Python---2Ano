lado=int(input('Digite o valor do lado do quadrado: '))
def calculo(lado):
    area_quadrado=lado**2
    return area_quadrado
area=calculo(lado)
print("A área do quadrado é de: ",area,"metros²")