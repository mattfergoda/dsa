class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        l_max = 0
        r_max = 0
        res_len = 0

        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    l_max = l
                    r_max = r
                    res_len = r - l + 1

                l -= 1
                r += 1

            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    l_max = l
                    r_max = r
                    res_len = r - l + 1

                l -= 1
                r += 1

        return s[l_max : r_max + 1]

