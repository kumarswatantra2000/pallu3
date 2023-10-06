n = int(input("Enter size of list:"))
list = []
for _ in range(n):
    num = int(input())
    list.append(num)
idx1 = int(input("entar index: "))
idx2 = int(input("Enter index:"))
print(list)


temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)