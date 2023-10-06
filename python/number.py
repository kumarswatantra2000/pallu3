def reverseNo1(n):
    #base case
    if n == 0:
        return
    print(n)
    reverseNo1(n-1)
    #print(n)
n = int(input("enter n: "))

reverseNo1(n)
