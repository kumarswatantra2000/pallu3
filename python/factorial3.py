def swatantra(n):

    # base case
    if n == 0:
        return 1
    # recursive method or call
    ans = n * swatantra(n-1)
    return ans
n = int(input("Enter n: "))
print(swatantra(n))
    