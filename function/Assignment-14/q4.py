# write a python program to create a function  check wheater a passed string is palindrem or not.

def pd():
    x=int(input("Enter a words \t"))
    y=x[::-1]
    print("yes, it is a palindrome " if y==x else "note a palindrome")
pd()