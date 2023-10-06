# REDUCE
import functools
l1=[1,2,3,4,5]
def pallu(a,b):
    return a*b
r=functools.reduce(pallu,l1)
print(r)
