#write a python script to print grater between two number. print number only once even if the number are the same

x=int(input("Enter a number \t"))
y=int(input("Enter a number \t"))
if (x==y):
    print("x is =",x,"y is =",y)
elif (x>y) :
    print("x is Greater then y")
else :
    print("y is greater")
