n=input("enter no")
for i in range(n):
    count=0
    for j in range(n-i-1):
        print (""),
    for j in range(0,i+1):
        print "*",
        if count<i:
            print "A",
            count=count+1
    print ""