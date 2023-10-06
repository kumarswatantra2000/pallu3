def push(num,n):
    num.append(n)
    return num

def pop(num):
    if isEmpty():
        return False
    else:
        num.pop()
        return num
def isEmpty(num):
    if not num:
        return True
    else :
        return False

num = []
push(num,2)
push(num,3)
push(num,4)
push(num,5)
push(num,6)
print(num)
