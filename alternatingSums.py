def alternatingSums(a):
    count1 = 0
    fleg = 0
    ar = []
    count2 = 0
    for i in range(0,len(a)):
        if i == 0:
            count1=count1+a[i]
        elif i%2==0:
            count1=count1+a[i]
        else:
            count2 = count2 + a[i]
    ar.append(count1)
    ar.append(count2)
    
    for j in range(len(ar)-1):
        if ar[j]>ar[j+1]:
            fleg = 1  
        else:
            ar[j],ar[j+1] = ar[j+1],ar[j]

    return ar

print alternatingSums([100, 51, 50, 100])