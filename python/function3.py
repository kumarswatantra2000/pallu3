# writing a function for calculating sum from 1 to n
def sumOneTwo(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum

n = int(input("Enter n: "))
#call function
output = sumOneTwo(n)
print("sum of all number n is", output)
n1 = int(input("Enter n: "))
output1 = sumOneTwo(n1)
print("sum of all number till n is", output1)