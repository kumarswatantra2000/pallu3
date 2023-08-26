#write a python scriopt to check wheather a given number is a three digit number or not.

x=int(input("Enter a number \t"))
y=("Three Digit Number" if 99<x<1000 else "not Three Digit")
print(y)