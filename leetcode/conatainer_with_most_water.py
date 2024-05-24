# https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area

