#  Data I/O
f=open("stuff.txt","r")
x=f.read()
for i in x:
    print(i,end=' ')
# print(f.readlines())

f.close()