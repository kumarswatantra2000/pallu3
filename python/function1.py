# write a function that prints hello world

#def printHello():
 #   # body of function
  #  print("hello world!")

#printHello()

# function wich take 2 number as input and return their sum

def add(n1, n2):
    print("n1:", n1)
    print("n2:", n2)
    sum = n1+n2
    return sum
# positional argument
#print("the sum is", add(2,3))

# keyword argument(named argument)
#print("the sum is", add(n2=2, n1=3))

#defoult arguments
#print("The sum is", add())
 # arbitrary arguments
def addAllNumber(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
#pallu = addAllNumber(1,2,3,4,5)
#print("the sum is", pallu)

# kw
def studentsInfo(**kwargs):
    for x,y in kwargs.items():
        print(x, "is",y)
studentsInfo(name="swatantra", age=22, city="patna")
studentsInfo(name="pallu", age=21, city="barh")
