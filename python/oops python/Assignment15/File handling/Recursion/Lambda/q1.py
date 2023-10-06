# write a python program to recursive function to print cubes of first N natural Number

def pallu(n):
    if n>0:
        print(n*n*n+pallu(n-1))
        pallu(n)

s=pallu(5)
print(s)


    
    