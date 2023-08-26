'''
write a python script 
a. write a python script 




'''
a=("press '1' for Isoscles triangle")
b=("press '2' for right Angled Triangle")
c=("press '3' for Equilateral Triangle")
print(a,b,c,sep="\n")
sides=int(input("choose you operation\t"))
print(sides)
match sides:
    case 1:
        x=int(input("Enter a 1st number\t"))
        y=int(input("Enter a 2nd number\t"))
        z=int(input("Enter a 3rd number\t"))
        if x==y or y==z or z==x:
            print("Isoscles triangle")
        else :
            print("not An Isoscles tringle")
    case 2:
        x=int(input("Enter a 1st number\t"))
        y=int(input("Enter a 2nd number\t"))
        z=int(input("Enter a 3rd number\t"))
        if x**2+y**2==z**2:
            print("Right Angled Triangle")
        else :
            print("Not a right Angled Triangle")
    case 3:
        x=int(input("Enter a 1st number\t"))
        y=int(input("Enter a 2nd number\t"))
        z=int(input("Enter a 3rd number\t"))
        if x==y and y==z :
            print("Equilateral Triangle")
        else :
            print("Not An Equilateral Triangle")
    case _:
        print("invalid")

            

     
