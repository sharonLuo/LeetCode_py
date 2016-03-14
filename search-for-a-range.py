"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""



class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin, end = 0, len(nums)-1
        while begin <= end:
            mid = (begin+end)/2
            if nums[mid] < target:
                begin = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                list = [0, 0]
                if nums[begin] == target: list[0] = begin
                if nums[end] == target: list[1] = end
                for i in range(mid, end+1):
                    if nums[i] != target: list[1] = i - 1; break
                for i in range(mid, begin-1, -1):
                    if nums[i] != target: list[0] = i + 1; break
                return list
        return [-1,-1]
                
        
        