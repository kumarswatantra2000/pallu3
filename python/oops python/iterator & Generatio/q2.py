#  Accessing Each Element of a container using while Loop-> Without Getting an Error.

t1=[23,4,56,78,45]
it=iter(t1)
#print(it)
while True:
    try:
        print(next(it),end=' ')
    except StopIteration:
        break
print(type(it))