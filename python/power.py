def swatantra(a,b):
     
    # base case
    if b == 0:
          return 1
    #recursive call
    pallu = a * swatantra(a, b-1)
    return pallu
a=int(input("Enter n a:"))
b=int(input("Enter n b:"))
print(swatantra(a,b))

     