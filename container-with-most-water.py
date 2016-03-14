"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""


Las Vegas, NV - LASclass Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0;
        right = len(height)-1;
        rst = 0
        while left < right:
            water = min(height[left], height[right])*(right-left)
            if water > rst:
                rst = water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return rst
        