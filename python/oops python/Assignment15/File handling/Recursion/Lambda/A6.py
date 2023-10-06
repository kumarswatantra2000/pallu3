#write a Recursion Function to sum Squares of N Natural Number

def sqs(n):
    if n==1:
        return 1
    
    a=n*n+sqs(n-1)
    return a
x=sqs(5)
print(x)    