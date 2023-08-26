''''
wriite a python script to check wheather a given year is a leai year or not
'''

a=int(input("Enter a number \t"))
if (a%100==0) and (a%4==0):
    print("Leap year")
elif (a%4==0) :
    print("lreap year")
elif (a%100==0) and (a%4==0) :
    print(" not leap year")
else :
    print("not a leap year")


      