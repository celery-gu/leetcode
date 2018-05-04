class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s=[]
        n=str(num)
        dict={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        a=int(num/1000)
        b=int((num%1000)/100)
        c=int((num%100)/10)
        d=int(num%10)
        if a!=0:
            s.append(Solution.insertS(a,1000,dict))
        if b!=0:
            s.append(Solution.insertS(b, 100, dict))
        if c!=0:
            s.append(Solution.insertS(c, 10, dict))
        if d!=0:
            s.append(Solution.insertS(d, 1, dict))
        #print(s)
        return "".join(s)

    def insertS(self,t,n,dict):
        k=[]
        if t==9:
            k.append(dict[n*10])
            k.insert(0,dict[n])
            t=t-9
        if t>=5:
            k.append(dict[n*5])
            t=t-5
        if t==4:
            k.append(dict[n*5])
            k.insert(0,dict[n])
            t=t-4
        if t>0 and t<4:
            while t>0:
                k.append(dict[n])
                t=t-1
        if t==0:
            return "".join(k)


num=1994
print(Solution.intToRoman(num))

