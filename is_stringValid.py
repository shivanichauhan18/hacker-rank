a="aacbbd"
dict={}
for i in a:
    count=0
    for j in a:
        if i==j:
            count=count+1
            dict[i]=count
print dict