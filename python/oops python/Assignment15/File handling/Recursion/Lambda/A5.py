# write a python script Recursive function are used to sum of natural number

def x1(n):
    if n==1:
        return 1
    x=n+(n-1)
    return x
s=x1(5)
print(s)