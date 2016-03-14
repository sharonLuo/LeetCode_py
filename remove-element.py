
"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        current = 0
        new_length = 0
        size = len(nums)
        for i in range(size):
            if nums[i] != val:
                nums[new_length] = nums[i]
                new_length += 1
        return new_length
        


"""        
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        current = 0
        last = len(nums)-1 
        while current <= last:
            if nums[current] == val:
                while nums[last] == val:
                    last -= 1
                nums[current], nums[last] = nums[last], nums[current]
                last -= 1
            current += 1
        return nums[0:(last+1)]
"""        

