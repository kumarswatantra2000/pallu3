#write a python to find the greatest number in a given list of number
x=int(input("Enter length of list of number \t"))
i=1
l1=[]
while (i<=x):
    l1.append(int(input("Enter values")))
    i+=1
print(max(l1))
