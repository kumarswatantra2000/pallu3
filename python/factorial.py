# function for creating factorial of a number

def factorial(n):
    pallu = 1
    if n == 0:
        pallu = 1
    else:
        for i in range(1, n+1):
            pallu += i

    return pallu

n = int(input("Enter n:"))
output = factorial(n)
print("factorial number in integer:", output)
