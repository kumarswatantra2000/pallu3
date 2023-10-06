# write a python script to first N even natural number.

x=int(input("Enter a number \t"))
for y in range(2,x*2+1,2):
    print(y ,end=' ')