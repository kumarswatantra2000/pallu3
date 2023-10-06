## Functioon definition
def searchSortedMatrix(matrix, target):
    ##number of row
    m = len(matrix)
    if m == 0:
        return False
    ## number of columns
    n = len(matrix[0])
    
    left, right = 0, m*n-1
    while left <= right:
        mid = left + (right - left)//2
        mid_element = matrix[mid//n][mid%n]
        if target == mid_element:
            return True
        elif target < mid_element:
            right = mid - 1
        else:
            left = mid + 1
    return False
# Druver code
matrix = [[1,3,5,6],[4,5,67,89],[32,45,67,87]]
target = 3
## Function colling
result = searchSortedMatrix(matrix, target)
print(result)