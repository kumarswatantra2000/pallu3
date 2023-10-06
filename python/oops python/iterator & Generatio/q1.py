# Accessing Each Element of a container using while Loop

t1=[23,4,56,78,45]
it=iter(t1)
#print(it)
while True:
    print(next(it),end=' ')
print(type(it))