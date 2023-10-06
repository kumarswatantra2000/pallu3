def add(m):
    if m==1:
        return 1
    x=m+add(m-1)
    return x