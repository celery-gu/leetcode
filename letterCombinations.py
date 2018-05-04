def letterCombinations(digits):
    list=[" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    if len(digits)==0:
        return []
    path,result="",[]
    begin=0
    helper(digits,begin,path,result,list)
    return result

def helper(digits,begin,path,result,list):
    if len(path)==len(digits):
        result.append(path)
        return
    for i in list[int(digits[begin])]:
        path+=i
        helper(digits, begin+1, path, result, list)
        path=path[:-1]


digits="23"
print(letterCombinations(digits))