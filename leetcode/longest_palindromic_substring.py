class Solution(object):
    def isPalindrome(self, s):
            if len(s) == 0:
                return False

            l = 0
            r = len(s) - 1
            mid = len(s) // 2

            while l < mid:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1

            return True
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 1:
            return s
        
        r = 1
        max_len = 0
        palindrome = ""

        for l in range(len(s)):
            for r in range (l + 1, len(s)):
                if self.isPalindrome(s[l:r]) and len(s[l:r]) > max_len:
                    max_len = len(s[l:r])
                    palindrome = s[l:r]

        return palindrome