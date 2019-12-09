def repeatedString(s, n):
    b=len(s)
    for k in range(0,b):
        count=0
        j=0
        for i in range (len(s),n+1):
            if len(s)==n:
                for i in s:
                    if i=="a":
                        count=count+1
            else:
                s=s+s
                j=j+1
                if j==b:
                    j=0
        else:
            break
    return count
print repeatedString("a",1000000000000)