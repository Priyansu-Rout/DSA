class Solution(object):
    def isPalindrome(self, x):
        strg = str(x)
        return strg == strg[::-1]