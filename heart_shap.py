for i in range(6):
    for j in range(7):
        if j % 3!=0 and i==0:
            print "*",
        elif j%3 ==0 and i==1:
            print "*",
        elif i-j==2:
            print "*",
        elif i+j==8:
            print "*",
        else:
            print " ",
    print " "