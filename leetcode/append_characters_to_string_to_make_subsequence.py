class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        s_pointer = 0
        t_pointer = 0
        res = 0

        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                t_pointer += 1

            else:
                res = max(res, t_pointer)
            s_pointer += 1

        res = max(res, t_pointer)
        
        return len(t) - res