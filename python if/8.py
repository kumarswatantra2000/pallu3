#write a python script to check wheather a given quadrative equation has two real & distance root real &equal roots or imaginary roots


a=int(input("Enter a number \t"))
b=int(input("Enter a number \t"))
c=int(input("Enter a number \t"))
d=b**2-4*a*c
if (d>0) :
    print("two real & distinct roots")
elif (d==0) :
    print("real & equal roots")
else :
    print("imaginary Roots")