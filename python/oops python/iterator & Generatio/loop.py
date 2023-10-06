def swatantra(n):
    i=1
while i<=n:
    j=1
    while j<=i:
        print('*',end='')
        j+=1
    print()
    i+=1
n=int(input("Enter a number\t"))
swatantra(n)