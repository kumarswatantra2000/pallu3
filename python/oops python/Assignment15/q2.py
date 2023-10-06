# write a python script to calculate sum of Square of first n natural number

x=int(input("Enter a number\t"))
sum=0
for y in range(x+1):
    sq=y**2
    sum=sum+sq
print(sum)