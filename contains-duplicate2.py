"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        mp = {}
        for inx in range(len(nums)):
            if mp.get(nums[inx]) == None:
                mp[nums[inx]] = inx
            elif (inx - mp[nums[inx]]) <= k:
                return True
            else:
                mp[nums[inx]] = inx
        return False
         