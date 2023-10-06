##Definition function
## time complextity:0(log n)
def binarySerach(arr, i, j, x):
    while 1 <= j:
        mid = i +(j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]  < x:
            i = mid+1
        else:
            return binarySerach(arr, 1, mid+1, x)
    return -1
##drive code
##sorted array
arr = [2, 5, 10, 14, 18, 22, 27, 35, 40, 59]
x =59
i = 0
j = len(arr)
##function calling
result = binarySerach(arr, i, j, x)
print("sraching element is at the index", result)