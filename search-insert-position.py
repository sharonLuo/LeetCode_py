"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

### 更简洁
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left = 0; right = len(A) - 1
        while left <= right:
            mid = ( left + right ) / 2
            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                return mid
        return left          
      

### 容易理解
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin, end = 0, len(nums)-1
        if target > nums[end]: return end+1
        if target < nums[begin]: return 0
        while begin <= end:
            mid = (begin+end)/2
            if nums[mid] < target:
                if nums[mid+1] > target:
                    return mid + 1
                begin = mid+1
            elif nums[mid] > target:
                if nums[mid-1] < target:
                    return mid
                end = mid-1
            else: 
                return mid

                
              