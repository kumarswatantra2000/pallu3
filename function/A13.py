# Average of 2 number

#def pallu(a,b):
 #   x=(a+b)/2
  #  return x
#print(pallu(3,2))

def pallu(*t):
    x=sum(t)/len(t)
    return x
print(pallu(7,7,7,7,.7,7,7,6,6,6,6,8,))