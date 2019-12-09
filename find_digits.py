def findDigits(n):
  j=0
  count=0
  a=str(n)
  for i in a:
    j=int(i)
    if i=="0":
        return 3
    elif n%j==0:
        count=count+1
    else:
        return 3
  return 2
  
  
element=input("eter number")
print findDigits(element)