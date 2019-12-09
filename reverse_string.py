def reverse(str):
    reverse=""
    for i in str:
        if i=="":
            print ""
        else:
            reverse=i+reverse
    print "your reverse value is ",reverse
str=raw_input("enter string")
reverse(str)