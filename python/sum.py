def swatantra(n):
    # base case
    if n == 1:
        return 1
    # recursive case
    ans = n + swatantra(n-1)
    return ans
n=int(input("Enter a n:"))
print(swatantra(n))

    

        