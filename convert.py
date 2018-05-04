def convert(s, numRows):
    matrix=[[0 for i in range(numRows)]for i in range(int(len(s)/2)+1)]
    num=0
    y=0
    if numRows==1:
        return s
    for i in range(int(len(s)/2)+1):
        if num<len(s):
            if i==0 or i%(numRows-1)==0:
                y = numRows - 1
                for j in range(numRows):
                    if num>=len(s):
                        break
                    matrix[i][j] = s[num]
                    num=num+1
            else:
                matrix[i][y-1]=s[num]
                num=num+1
                y=y-1
    ans=""
    for j in range(numRows):
        for i in range(int(len(s)/2)+1):
            if(matrix[i][j]!=0):
                ans+=matrix[i][j]
    return ans

s = "PAYPALISHIRING"
numRows = 2
print(convert(s,numRows))