"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] <= 0:
                i += 1
            elif nums[i] == i+1:
                i += 1
            else:
                nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        i = 0
        while i < len(nums):
            if i+1 != nums[i]:
                break
            i += 1
        return i+1
        
