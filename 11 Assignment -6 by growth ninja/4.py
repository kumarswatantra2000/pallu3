'''
write a program which takes user s Age and display the categry of persons. age below 10 years- kind agebelow 
20years-teen, Age below 40- young beliow 60 years - Expend, Age above or equal 60 - senior Citilzen
'''
age=int(input("Enter is your age\t"))
print(age)
match age:
    case age if age<=10:
        print("kid")
    case age if 10<age<=20:
        print("Teen")
    case age if 20<age<=40  :
        print("young")
    case age if 40<age<=60:
        print("Expend")
    case age if 60<age<=60:
        print("Senior Citilizen")
    case _:
        print("indivi")

    
        
