def myAtoi(str):
    s=''
    for x in str:
        if x.isdigit():
            s=s+x
        elif ((x=='-' or x=='+')and s==''):
            s=s+x
        elif x=='-' or x=='+':
            break
        elif x==' ' and s=='':
            pass
        else:
            break
    if s=='' or s=='-' or s=='+':
        return 0
    t=int(s)
    if t<-2147483648:
        return -2147483648
    if t>2147483647:
        return 2147483647
    return t

str="0-1"
print(myAtoi(str))