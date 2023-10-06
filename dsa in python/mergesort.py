##def mergeProedure(arr, i, mid, j):
def mergeProcedure(arr, i, mid, j):
    #3 n1-> number of element in the left array
    n1 = mid - i + 1
    ## n2 -> number of element in the right subarray
    n2 = j - mid
    ## Driver code for left side subarray and right subarray
    leftSubarray = [0] * n1
    rightSubarray = [0] * n2


    ## copy the element from an areray to the subarray
    for m in range(n1):
        leftSubarray[m] = arr[i + m]
    
    for n in range(n2):
        rightSubarray[n] = arr[mid + 1 + n]
    p = 0
    q = 0
    k = 1

    while p < n1 and q < n2:
        if leftSubarray[p] <= rightSubarray[q]:
            arr[k] = leftSubarray[p]
            p += 1
        else:
            arr[k] = rightSubarray[q]
            q += 1
        k += 1
    
    ## copy the enter element from left subarray
    while p < n1:
        arr[k] = leftSubarray[p]
        p +=1
        k += 1
    ## copy the enter element from the right subarray
    while q < n2:
        arr[k] = rightSubarray[q]
        q += 1
    
        k += 1
## function defintion
def mergeSort(arrr, i, j):
    if i < j:
        mid = i + (j - i)//2
        ## Recursive function call
        mergeSort(arr, i, mid)
        mergeSort(arr, mid+1, j)
        ## combine
        mergeProcedure(arr, i, mid, j)
    return arr
## Drive code
arr = [50, 70, 65, 13, 80, 62, 98, 27]
i = 0
j = len(arr) - 1
result = mergeSort(arr, i, j)
print("sorted array og merge sort is:", result)