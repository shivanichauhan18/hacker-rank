alphabet=65
for i in range(1,5+1):
    for j in range(1,5-i+1):
        print (""),
    for j in range(0,i):
        print chr(alphabet),
        alphabet=alphabet+1
    print " "
