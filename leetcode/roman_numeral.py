class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        subtraction = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        pointer = 0
        res = 0

        while pointer < len(s):

            if pointer < len(s) - 1 and s[pointer] + s[pointer + 1] in subtraction:
                res += subtraction[s[pointer] + s[pointer + 1]]
                pointer += 2
            else:
                res += nums[s[pointer]]
                pointer += 1

        return res


