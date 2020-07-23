
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for i in strs:
            dic[''.join(sorted(i))].append(i) #这里是因为sorted返回值是一个list dic的键不能是list 要用.join变成字符串

        return list(dic.values())


s = Solution()

strs =["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))

