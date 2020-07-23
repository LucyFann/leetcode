class Solution:
    def reverse(self, x):
        if x<0:
            y = -1*int(str(-x)[::-1])
        else:
            y = int(str(x)[::-1])
        if y > 2147483648 or y < -2147483648 :
            y = 0
        return y

s = Solution()
print(s.reverse(-18))