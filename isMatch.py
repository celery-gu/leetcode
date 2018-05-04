def isMatch(s, p):
    k=0
    if not p:
        return bool(s)
    if len(p)>1 and p[1]=='*':
        return isMatch(s,p[2:]) or ()


