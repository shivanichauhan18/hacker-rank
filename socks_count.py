def sockMerchant(n, ar):
    arr1=[]
    i=0
    count_socks=0
    while i<n:
        count=0
        for j in range(i,n):
            if ar[i]==ar[j] and ar[i] not in arr1:
                count=count+1
                if count==2:
                    count_socks=count_socks+1
                    count=0
        arr1.append(ar[i])
        i=i+1
    return count_socks
print sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])