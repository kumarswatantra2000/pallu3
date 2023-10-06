ar1 = [1,2,3,3,10]
ar2 = [3,4,5,6,7,8,10]
ar3 = [3,3,3,10,20]

#type casting into sets
s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

# join using intersection_updade
s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)

print(final_set)
