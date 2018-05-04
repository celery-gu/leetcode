def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for x in nums:
        t=target-x
        if t in nums:
            a=nums.index(x)
            nums[a]=-10000000000000
            try:
                b=nums.index(t)
                r = []
                if a!=b:
                    r.append(a)
                    r.append(b)
                    return r
            except:
                pass

nums = [0,4,3,0]
target=0
answer=twoSum(nums,target)
print(answer)