"""
LeetCode 题解 2.1.4 search in a rotated sorted array II
follow up for "search in rotated sorted array". What if duplicates are allowed?
Would this affect the run-time complexity? How and Why?
Write a function to determine if a given target is in the array

允许重复元素,则上题中 A[m] >= A[l]代表的[l,m]为递增序列的假设就不能成立了,比如[1,3,1,1,1].
如果 A[m] > A[l], 则区间一定递增
如果 A[m] = A[l]确定不了,则l++, 往下一步即可
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        first, last = 0, len(nums)-1
        while first <= last:
            mid = (first+last)/2
            if target == nums[mid]:
                return True
            if nums[first] < nums[mid]:
                if target >= nums[first] and target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            elif nums[first] > nums[mid]:
                if target > nums[mid] and target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid - 1
            else:
                first += 1
        return False
                
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        first, last = 0, len(nums)-1
        while first <= last:
            mid = (first+last)/2
            if target == nums[mid]:
                return True
            if nums[mid] < nums[last]:
                if target > nums[mid] and target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid -1
            elif nums[mid] > nums[last]:
                if target >= nums[first] and target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:
                last -= 1
        return False
                
                
                        
        
        
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
        	if nums[first] < nums[mid]:
        		if target >= nums[first] and target < nums[mid]:
        			last = mid -1
        		else:
        			first = mid + 1
        	elif nums[first] > nums[mid]:
        		if target > nums[mid] and target <= nums[last]:
        			first = mid + 1
        		else:
        			last = mid -1
        	else:
        		first += 1
        return -1


