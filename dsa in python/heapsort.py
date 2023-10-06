from collections import Counter 
import heapq
## function definition
def topkfreqentElement(arr, 'k'):
    if k == len(arr):
        return set(arr)
    
    count = Counter(arr)
    print(count)
    return heapq.nlargest(k, count.keys(),key=count.get)

## Drive code
arr = [1,1,1,1,2,2,2,3]
k = 2
## function callng
result = topkfreqentElement(arr)
print("the heap sort are the sorted in bunary search tree:", result)