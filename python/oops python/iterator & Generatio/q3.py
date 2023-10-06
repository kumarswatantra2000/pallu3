t1=[12,345,34,56,778,45,23]
it=iter(t1)
i=1
while i<=5:
    print(next(it),end=' ')
    i+=1
print(type(it))