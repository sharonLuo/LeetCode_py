"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""

##### O(n) 滑动窗口
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        start, end, sums = 0, 0, 0
        bestAns = size + 1
        while end < size:
            while end < size and sums < s:
                sums += nums[end]
                end += 1
            while start < end and sums >= s:
                bestAns = min(bestAns, end-start)
                sums -= nums[start]
                start += 1
        return [0, bestAns][bestAns <= size]



#### O(n log n)
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        left, right = 0, size
        bestAns = 0
        while left <= right:
            mid = (left + right) / 2
            if self.solve(mid, s, nums):
                bestAns = mid
                right = mid - 1
            else:
                left = mid + 1
        return bestAns

   
    def solve(self, l, s, nums):
        """
        this function check whether a subarray of length l could have sums larger than target s
        l control the length of subarray
        """
        sums = 0
        for x in range(len(nums)):
            sums += nums[x]
            if x >= l:  ### if the subarray length is larger than l, then need to subtract the extra head part
                sums -= nums[x - l]
            if sums >= s:
                return True
        return False


######## O(n log n)
