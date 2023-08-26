'''
Write a python which takes a number from user . print Swatantra kumar if the numbver
a given print preteek jain if the number is negative and number odd number and print pallu kumart rajakif number is positive odd number
'''
a=int(input("Enter a number\t"))
print(a)
match a:
    case a if a%2==0:
        print("swatantra kumar")
    case a if a<0 and a%2:
        print("Negative odd Number")
    case a if a%2:
            print("pallu kumar rajak")
        

