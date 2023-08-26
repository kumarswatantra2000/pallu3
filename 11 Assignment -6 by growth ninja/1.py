x=int(input("Enter a value of month \t"))
match x:
    case x if x in (1,3,5,7,8,10,12):
        print("31 days")
    case x if x in (4,6,9,11):
        print("30 days")
    case x if x==2:
        print("28 or 30 days")
    case _:
        print("invalid")

      
