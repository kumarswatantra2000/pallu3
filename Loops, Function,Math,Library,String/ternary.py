## function definition
def ternarySearch(l,r,x,arr):
    while l <= r:
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3
        
        if x == arr[mid1]:
            return mid1
        elif x == arr[mid2]:
            return mid2
        elif x < arr[mid1]:
            return ternarySearch(l, mid1-1, x,arr)
        elif x > arr[mid2]:
            return ternarySearch(mid2+1, r, x, arr)
        else:
            return ternarySearch(mid1+1, mid2-1, x, arr)
    return -1
## Drive code
arr = [1,2,3,4,5,6,7,8,9,10]
l = 0
r = len(arr) - 1
x = 2
result = ternarySearch(l, r, x, arr)
print("searching element is persent at index", result)