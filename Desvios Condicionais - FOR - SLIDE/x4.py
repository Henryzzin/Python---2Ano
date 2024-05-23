for num in range (2,30):
    prime = True
    for j in range (2,num):
        if num % j == 0:
            prime=False
            break
    if prime==True:
        print(num)