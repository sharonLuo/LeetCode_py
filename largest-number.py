"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted(nums, cmp=self.my_cmp)
         
        if nums[0] == 0:
            return "0"
        else:
            return "".join([str(n) for n in nums])


    def my_cmp(self, x,y):
        sx = str(x)
        sy = str(y)
        sx = sx + sy
        sy = sy + sx
        if sx > sy:
            return -1
        if sx == sy:
            return 0
        if sx < sy:
            return 1
