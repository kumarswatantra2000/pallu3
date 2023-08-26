'''

'''
x=(input("Enter a string\t"))
y=(input("Enter a string\t"))
print(x)
match (x,y):
    case (x,y) if x==y:
        print("Indentical")
    case (x,y) :
        if x>y :
            print(y,x, sep="\n")
        else:
            print(x,y,sep="\n")
        
