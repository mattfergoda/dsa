class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x_str = str(x)

        for i in range(len(x_str)):
            if x_str[i] != x_str[len(x_str) - 1 - i]:
                return False

        return True