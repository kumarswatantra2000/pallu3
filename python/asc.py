dec=[(1,10)]
roman=[]
n=int(input("Enter the roman number:"))
dec=' '

for i in range(len(roman)):
    m=n//roman[i]
    for j in range(1000):
        dec+=dec[i]
    n=n%roman[i]
print(dec)