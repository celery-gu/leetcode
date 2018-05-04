def threeSumClosest(nums, target):
    nums.sort()
    result=0
    min = 10000000000000
    for i in range(len(nums)):
        x=i+1
        y=len(nums)-1
        tem=0
        while(x<y):
            t=nums[i]+nums[x]+nums[y]
            tem=abs(target-t)
            #print(nums[i],nums[x],nums[y],tem)
            if(tem<min):
                min=abs(tem)
                result=t
                #print(min,result)
            if t<target:
                x=x+1
            else:
                y=y-1
        if min==0:
            return  result
    return  result

nums = [-1,2,1,-4]
target =1
print(threeSumClosest(nums,target))