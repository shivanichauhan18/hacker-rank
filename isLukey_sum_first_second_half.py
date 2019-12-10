def isLucky(n):
    st = str(n)
    lis = list(st)
    
    a = len(lis) // 2
    
    list1 = lis[:a]
    
    list2 = lis[a:]
    count1= 0
    count2 = 0
    for i in range (0,len(list2)):
        count1 = count1 + int(list1[i])
        count2 = count2 + int(list2[i])
    if count1 == count2:
        return True
    else:
        return False

isLucky(123456)