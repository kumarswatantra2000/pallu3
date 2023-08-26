''''
write a python program to check wheather a given number is positive, neagative or zero using match cazse statements
'''

x=int(input("Enter a number"))
print(x)
match x:
    case x:
        if x==0:
            print("Zero")
        elif x<0 :
            print("negative")
        else :
            print("positive'+ve'")
