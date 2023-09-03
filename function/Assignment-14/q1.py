# write a python program to create a function that takes a list and returns a new list with the original list unique elements

def lt(l):
    li=[]
    for x in l:
        if x not in li:
            li.append(x)
    return li
   #x=int(input("Enter a first list"))
print(lt([True,6,7.8,False,(4+5j),True,6]))
    