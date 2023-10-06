# Create a generator to produce first n terms of Fibonicci series

def fib(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1
            print(x,end=' ')

