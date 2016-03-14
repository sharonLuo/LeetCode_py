"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive_max, negative_min = [0]*(len(nums)+1), [0]*(len(nums)+1)
        positive_max[0], negative_min[0] = 1,1        
        for i in range(len(nums)):
            if nums[i] > 0:
                positive_max[i+1] = max(positive_max[i]*nums[i], nums[i])
                negative_min[i+1] = negative_min[i]*nums[i]
            elif nums[i] < 0:
                positive_max[i+1] = negative_min[i]*nums[i]
                negative_min[i+1] = min(positive_max[i]*nums[i], nums[i])
        return max(positive_max[1:])
            
        