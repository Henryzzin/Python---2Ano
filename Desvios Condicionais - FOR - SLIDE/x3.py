resultado=1
fator=int(input("Qual fatoria você deseja ver? "))
for num in range(1,fator):
    resultado=resultado*fator
    fator=fator-1
print("O resultado é de", resultado)