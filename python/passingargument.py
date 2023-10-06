# passing by value

def addOne(x):
    x = x + 1
    print("inside function:", x)

x = 5
addOne(x)
print("Outside function:", x)
# pass by reference

def modifiList(list):
    lst.append(4)
    print("inside function:", lst)


lst = [1,3,4]
modifiList(lst)
print("outside function",lst)