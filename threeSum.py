
def threeSum(nums):
    result=[]
    nums.sort()
    for i in range(len(nums)):
        if nums[i]>0:
            break
        if i>0 and nums[i]==nums[i-1]:
            continue
        target=0-nums[i]
        x=i+1
        y=len(nums)-1
        while(x<y):
            if nums[x]+nums[y]==target:
                result.append([nums[i],nums[x],nums[y]])
                while x<y and nums[x]==nums[x+1]:
                    x=x+1
                while x < y and nums[y] == nums[y - 1]:
                    y=y-1
                x=x+1
                y=y-1
            elif nums[x]+nums[y]<target:
                x=x+1
            else:
                y=y-1
    return result

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))