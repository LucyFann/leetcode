import pdb
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        dic = {}
        start = 0
        for i in range(len(s)):
            cur = s[i]
            if cur not in dic.keys():
                dic[cur] = i
            else:
                if dic[cur]+1>start:
                    start = dic[cur]+1
                dic[cur] = i
            if dic[cur]-start+1>l:
                l = dic[cur]-start+1
        return l


S = Solution()
s = "abba"
print(S.lengthOfLongestSubstring(s))