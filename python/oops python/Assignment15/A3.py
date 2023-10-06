# Filter
l1=['a','e','i','o','u']
r1=['s','w','a','t','a','n','t','r']

def pallu(variable):
    if (variable in l1):
        return True
    else:
        return False
x=list(filter(pallu,r1))
print(x)