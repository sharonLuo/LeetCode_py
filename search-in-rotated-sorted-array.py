
"""
LeetCode 题解 2.1.3 search in a rotated sorted array
Suppose a sorted array is rotated at some pivot unknown to you beforehand
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2)
you are given a target value to search. If found in the array return its index, otherwise return -1
you may assume no duplicate exists in the array

利用二分法, 难度在于左右边界的确定

time O(lg n), space O(1)
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, last = 0, len(nums)-1
        while first <= last:
        	mid = (first+last)/2
        	if target == nums[mid]:
        		return mid
        	if nums[first] <= nums[mid]:
        		if target >= nums[first] and target < nums[mid]:
        			last = mid -1
        		else:
        			first = mid + 1
        	else:
        		if target > nums[mid] and target <= nums[last]:
        			first = mid + 1
        		else:
        			last = mid -1
        return -1


