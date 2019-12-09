arr=[1,2,3,4,5,6,7,8]
arr1=[1,2,5,3,4,7,8,6]
count=0
for i in range(1,len(arr)-1):
    a=len(arr)-1
    for j in range(1,len(arr1)-1):
        b=len(arr1)-1
        if arr[a]==arr1[b]:
            print "sahi hai"
            break
        else:
            count=count+1


# updated arr

arr=[1,2,3,4,5,6,7,8]
arr1=[1,2,5,3,4,7,8,6]
count=0
ar=[]
for i in range(0,len(arr)-1):
    a=len(arr)-i-1
    for j in range(i,len(arr1)-1):
        b=len(arr1)-j-1
        if arr[a]==arr1[b]:
            ar.append(b)
            print "sahi hai"
            break
        else: 
            for k in range(0,len(ar)):
                if b == ar[k]:
                    break
            else:
                count=count+1
print count
print ar