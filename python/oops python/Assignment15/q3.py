# Write a python script to calculate sum of cubes of first N natural number

x=int(input("Enter a number\t"))
sum=0
for y in range(x+1):
    sq=y**3
    sum=sum+sq
print(sum)
