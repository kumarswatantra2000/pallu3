'''
write a python program to check wheather a given string is a multiword string or single word string using mathch case statement
'''
x=input("Enter a words\t")
print(x)
match x:
    case x :
        if ' ' in x:
            print("muliwords string")
        else :
            print("single word string")

