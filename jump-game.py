"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""



class Solution(object):
    def canJump(self, nums):
        canReach = 0
        for i in range(len(nums)):
            if i <= canReach:
                canReach = max(canReach, i + nums[i])
                if canReach >= len(nums) - 1: return True
        return False



class Solution(object):
    def canJump(self, nums):
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else: # no enough step to move forward
                return False
        return True
