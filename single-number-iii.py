"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for ele in nums:
            diff ^= ele
        diff &= -diff
        ans = [0,0]
        for ele in nums:
            if ele & diff == 0:
                ans[0] ^= ele
            else:
                ans[1] ^= ele
        return ans
        

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, filter(lambda x : x & xor & -xor, nums))
        return [ans, ans ^ xor]

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, (x for x in nums if x & xor & -xor))
        return [ans, ans ^ xor]
        
