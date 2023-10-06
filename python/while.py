'''
x = 1
while x == 1:
    x = x-1
    print(x)

i = 10
while i - 20:
    print("swatantra")

x = 4 
y = 0
while x>=0:
    x-=1
    y+=1
    if x==y:
        continue 
    else:
        print(x,y)

x = 4
y = 0
while x>=0:
    if x==y:
        break
    else:
        print(x, y)
    x-=1
    y+=1

n = int(input("Enter n: "))
for i in range(n):
    print("*" * 5)

n = int(input("Enter n: "))
for i in range(n):
    for j in range(1, n+1):
        print(j, end="")
    print()

n= int(input("Enter n:"))
for i in range(1, n+1):

    for j in range(1, i+1):
        print(j, end="")
    print()
    
n= str(input("Enter n:"))
for i in range(1, n+1):

    for j in range(1, i+1):
        print(j, end="")
    print()

n = int(input("Enter a number:"))
for i in range(1, n+1):
    # print spaces
    print(" " * (n-i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()
    '''
n = int(input("Enter a number:"))
for i in range(1, n+1):
    # print spaces
    print(" " * (n-i), end="")
    for j in range(1, 3 * i):
        print(j, end="")
    print()
    






