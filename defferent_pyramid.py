user=40
start=1
for i in range(1,9):
    ar=[]
    for j in range(0,i):
        if i%2==0 and start<=user:
            ar.append(start)
        elif start<=user:
            print start,
        start=start+1
        
    b=len(ar)-1
    while b>=0:
        print ar[b],
        b=b-1
    print ""