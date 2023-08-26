#write a python script to create a list of first even natural number
x=int(input("Enter a value 'n'\t"))
l1=[]
for x in range(2,x*2+1,2):
    l1.append(x)
print(l1)