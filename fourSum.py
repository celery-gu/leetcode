# class solution(object):
#     def foursum(self,nums, target):
#         nums.sort()
#         path = []
#         result = []
#         begin = 0
#         self.helper(path, result, begin, nums, target)
#         result=list(set(t for t in result))
#         for i in range(0, len(result)):
#             result[i] = list(result[i])
#         return result
#
#     def helper(self, path, result, begin, nums, target):
#         if len(path) == 4 and target == 0:
#             result.append(tuple(path))
#             # print(result)
#             return
#         if len(path)==4:
#             return
#         t = target
#         for i in range(begin, len(nums)):
#             if  target<0 and nums[i]>0:
#                 break
#             target -= nums[i]
#             path.append(nums[i])
#             self.helper(path, result, i + 1, nums, target)
#             path.pop()
#             target = t

def foursum(nums, target):
    result=[]
    nums.sort()
    t=target
    for i in range(len(nums)):
        for j in  range(i+1,len(nums)):
            target = t
            target=target-nums[i]-nums[j]
            x=j+1
            y=len(nums)-1
            while(x<y):
                #print(nums[i],nums[j],nums[x],nums[y],target)
                if nums[x]+nums[y]==target:
                    result.append([nums[i],nums[j],nums[x],nums[y]])
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
    result =list(set(tuple(t) for t in result))
    result=[list(t) for t in result]
    #print(result)
    return result

nums=[1,0,-1,0,-2,2]
target=0
foursum(nums,target)