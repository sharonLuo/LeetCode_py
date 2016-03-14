
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].


#### same idea as next solution
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        dir = 1
        for i in range(1, len(nums)):
            if dir==1:
                if nums[i]<nums[i-1]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                dir = -1
            else:
                if nums[i]>nums[i-1]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                dir = 1
        return
        


### order each two consecutive ((0,1),(2,3), ...) elements get <=, then for each set change the order to get >=
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for i in range(0, size-1, 2):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        i = 1
        while i < size and i+1 < size:
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2
        
  

### Time Limit Exceed
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for i in range(size):
            min_n = nums[i]
            min_inx = i
            for j in range(i+1, size):
                if nums[j] < min_n:
                    min_n = nums[j]
                    min_inx = j
            if min_inx != i:
                tmp = nums[i]
                nums[i] = nums[min_inx]
                nums[min_inx] = tmp
        i = 1
        while i < size and i+1 < size:
            tmp = nums[i+1]
            nums[i+1] = nums[i]
            nums[i] = tmp
            i += 2
        
        
            


