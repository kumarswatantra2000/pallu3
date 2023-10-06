# write a python script to calculate sum of first N odd natural number

x=int(input("Enter a number\t"))
sum=0
for y in range(1,x*2+1,2):
    
    sum+=y
print(sum)
