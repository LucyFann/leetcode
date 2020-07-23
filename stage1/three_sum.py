
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_hash = {}
        result = []
        for num in nums:
            nums_hash[num] = nums_hash.get(num,0)+1
        if 0 in nums_hash and nums_hash[0]>=3:
            result.append([0,0,0])
        nums = sorted(list(nums_hash.keys()))  #这一步很重要 对nums里面进行了去重 
        for i,a in enumerate(nums):
            for b in nums[i+1:]:
                if b*2+a==0 and nums_hash[b]>=2:
                    result.append([b,b,a])
                if a*2+b==0 and nums_hash[a]>=2:
                    result.append([a,a,b])
                dif=-a-b
                if dif in nums_hash and dif>b:
                    result.append([a,b,dif])
        return result

s = Solution()

nums = [-1,0,1,2,-1,-4]

print(s.threeSum(nums))