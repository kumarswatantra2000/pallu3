#  variable length Argument (list)
def avg(*l):
    x=sum(l)/len(l)
    return x
print(avg(2,3,5,56,7))