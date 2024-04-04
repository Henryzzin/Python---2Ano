x=float("Dê um valor a X: ")
y=float("Dê um valor a Y: ")
if (x+y)*0.3>500:
    z=x
    x=y
    y=z
else:
    if x>y:
        print(f"{x}")
    else: 
        print(f"{y}")