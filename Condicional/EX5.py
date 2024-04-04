comb=float(input("Se for álcool, digite 1. Se for gasolina digite 0. "))
litros=float(input("Quantos litros foram colocados?"))
if litros<=20:
    if comb==1:
        valor=(6.5*0.97)*litros
    else:
        valor=(7.2*0.96)*litros
else:
    if comb==1:
        valor=(6.5*0.95)*litros
    else:
        valor=(7.2*0.94)*litros
print(f"{valor}")