s="aba"
n=10
while  True:
    count=0
    j=0
    for i in range (len(s),n+2):
        if len(s)==n:
            for i in s:
                if i=="a":
                    count=count+1
        else:
            s=s+s[j]
            j=j+1
            if j==len(s)-1:
                j=0
