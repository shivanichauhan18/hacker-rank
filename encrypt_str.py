def reverse(str):
    b=len(str)-1
    str1=""
    while 0<=b:
        str1=str1+str[b]
        b=b-1
    return str1

def add_vowels(reverse_str):
    dict={"a":"0","e":"1","o":"2","u":"3","i":"2"}
    encrypt=""
    for i in reverse_str:
        if i in dict.keys():
            key=dict[i]
            encrypt=encrypt+key
        else:
            encrypt=encrypt+i
    return encrypt
        

def encrpt_str(value):
    adding_str="aca"
    reverseStr=reverse(value)

    encrpt_value=add_vowels(reverseStr)
    return encrpt_value+adding_str

str=raw_input("enter string  -")
print encrpt_str(str)
