class Solution:
    def twoSum(self, nums,target):
        dic={}
        for i,num in enumerate(nums):
            if num in dic:
                return [dic[num],i]
            else:
                dic[target-num]=i


s=Solution()

nums = [2, 7, 11, 15]
target = 9

print(s.twoSum(nums,target))