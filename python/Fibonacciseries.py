def swatantra(n):

    # base case
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (swatantra(n-1) + swatantra(n-2))
n = int(input("Enter a n: "))
for i in range(1, n+1):
    print(swatantra(i))