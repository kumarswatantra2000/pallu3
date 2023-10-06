def f1():
    yield 10
    print("*")
    yield 20
    print("***")
    yield 30
    print("2222")
x=f1()
print(next(x))
print(next(x))
print(next(x))
