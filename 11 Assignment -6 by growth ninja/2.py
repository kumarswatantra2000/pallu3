'''
calculator addition subtraction multiplication division
'''
a=("press '1' for Addition")
b=("press '2' for subtraction")
c=("press '3' for multiplication")
d=("press '4' for division")
print(a,b,c,d, sep="\n")
match=int(input("choose your Operations\t"))
print(match)
match (match) :
    case 1:
        print("Enter Value for Addition")
        x=int(input("Enter a Number\t"))
        y=int(input("Enter a number\t"))
        a_1=x+y
        print(a_1)
    case 2:
        print("Enter Value for Subtraction")
        x=int(input("Enter a Number\t"))
        y=int(input("Enter a number\t"))
        a_1=x-y
        print(a_1)
    case 3:
        print("Enter Value for Multiplication")
        x=int(input("Enter a Number\t"))
        y=int(input("Enter a number\t"))
        a_1=x*y
        print(a_1)
    case 4:
        print("Enter Value for Division")
        x=int(input("Enter a Number\t"))
        y=int(input("Enter a number\t"))
        a_1=x//y
        print(a_1)
    case _:
        print("invalid value")
    
