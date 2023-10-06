dec=[1000,900,500,400,100,90,40,10,9,5,4,1]
rom=['m','cm','d','cd','c','xc','xl','x','ix','v','iv',]
n=int(input("Enter the number :"))
rom= ' '

for i in range(len(dec)):
    m=n//dec[i]
    for j in range(m):
        rom+=rom[i]
    n=n%dec[i]
print(rom)