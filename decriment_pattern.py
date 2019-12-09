n=input("enter no")
for i in range(0,n):
    for j in range(0,n-i):
        print("*"),
    print ""


for i in range(0,n):
    for j in range(0,i+1):
        print("*"),
    print ""