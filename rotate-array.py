

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k:
            self.reverse(nums, 0, n-k)
            self.reverse(nums, n-k, n)
            self.reverse(nums, 0, n)
        
    def reverse(self, nums, begin, end):
        mid = (end+begin)/2 
        for inx in range(begin, mid):
            nums[inx], nums[begin+end-inx-1] = nums[begin+end-inx-1], nums[inx]
        
  
##############################################

  class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        
 ##############################################
 ### slow:
 class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        for i in range(k):
            nums.insert(0, nums.pop())
        
       
        
            
       

