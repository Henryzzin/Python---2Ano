total=0
for x in range (1,1001):
    total=0
    for a in range (1,x):
        if x%a==0:
            total=total+a
            if total==x and total!=24:
                print(total)