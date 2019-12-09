def rotLeft(a, d):
    for i in range(0,d):
        a.append(a[0])
        a.remove(a[0])
    return a
print rotLeft([1,2,3,4,5],4)
