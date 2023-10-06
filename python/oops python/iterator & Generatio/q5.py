# Use iter and next method to access all the element of a given set using while loop

s1={12,45,67,55,88,34}
it=iter(s1)
i=1
while i<=6:
  print(next(it),end=' ')
  i+=1 