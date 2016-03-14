"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


##### by xor
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = len(nums)
        for inx, e in enumerate(nums):
            rst ^= inx ^ e
        return rst
  

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = len(nums)
        for inx in range(len(nums)):
            rst ^= inx ^ nums[inx]
        return rst
        

####### by sum
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        return size*(size+1)/2-sum(nums)
  
  
