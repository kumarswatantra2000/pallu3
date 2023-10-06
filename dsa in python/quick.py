def quicksort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a.pop()

    greater = []
    lower = []

    for i in a:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)
    return quicksort(lower) + [pivot] + quicksort(greater)

l = [3,4,6,8,4,1,3,2,9,5,10]
print(quicksort(l))
    