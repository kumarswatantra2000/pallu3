# function are the used og factorial 
def factorial(n):
    ans = 1
    if n == 0:
        ans = 1
    else:
        for i in  range(1, n+1):
            ans += i
    return ans

n = int(input("Enter a number n: "))
output = factorial(n)
print("factorial is: ", factorial)