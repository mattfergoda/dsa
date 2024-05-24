# https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_area = 0

        for i in range(len(height)):
            h1 = height[i]
            for j in range(i, len(height)):
                h2 = height[j]
                area = min(h1, h2) * abs(j - i)
                if area > max_area:
                    max_area = area

        return max_area

