form heapq import heappush, heapop
import math
##function definition
def get_dist(x,y):
    return math.sqrt(x**2 + y**2)


def kClosest(points, k):
    n = len(points)
    for i in range(n):
        x = points[i][0]
        y = points[i][1]

        heappush(min_heap, (get_dist(x,y), points[i]))

    result = []
    for i in range(k):
        result.append(heappop(min_heap)[1])
    return result





## drive code 
points = [[3,3],[5,-1], [-2, 4]]
k = 2
result = kClosest(points, k)
print("k closest points to the origin are:", result)