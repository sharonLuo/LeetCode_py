"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.


"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x1 = x2 = 0x7fffffff
        for num in nums:
            print x1, x2
            if num <= x1:
                x1 = num
            elif num <= x2:  # x1 < num <= x2
                x2 = num
            else:            # x < x2 < num , so it return true
                return True
        return False
