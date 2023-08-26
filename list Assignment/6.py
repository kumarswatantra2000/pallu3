#write a python program to append element from another list to the current list(firstlist =["java","python","sql"])
firstlist =["java","python","sql"]
l1=["go log","Ruby","Docker","pallu"]
for x in l1:
    firstlist.append(l1)
    print(firstlist)