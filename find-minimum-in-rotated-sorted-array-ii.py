"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, last = 0, len(nums)-1
        while first < last and nums[first] >= nums[last]:
            mid = (first + last)/2
            if nums[mid] > nums[last]:
                first = mid + 1
            elif nums[mid] < nums[last]:
                last = mid
            else:
                first += 1
        return nums[first]
                
                