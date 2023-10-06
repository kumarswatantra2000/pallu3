def pallu(n):

    # base case
    if n== 0:
        return 1
    # recursive case
    ans = n * pallu(n-1)
    return ans

n = int(input("Enter n: "))
print(pallu(n))