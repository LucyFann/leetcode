import pdb
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        Palindrome = ''
        max_len = 0
        l = len(s)
        if l==1:
            return s
        for i in range(l):
            for j in range(i+1,l):
                is_Palindrome = True
                for k in range(i,(i+j)//2+1):
                    if s[k]!=s[j-k+i]:
                        is_Palindrome=False
                        break
                if is_Palindrome and (j-i+1)>max_len:
                    max_len = j-i+1
                    Palindrome = s[i:j+1]
        if Palindrome == '':
            Palindrome = s[0]
        return Palindrome



S = Solution()

s = "ab"

print(S.longestPalindrome(s))