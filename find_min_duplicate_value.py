function firstDuplicate(a):
    fleg=0
    ar=[]
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:   
                fleg=1
                ar.append(j)
    if fleg == 0:
        return -1
    k=0
    min=ar[0]
    while k<len(ar):
        if min>ar[k]:
            min=ar[k]
        k=k+1
    return a[min]

print firstDuplicate([1,2,3,4,5])

