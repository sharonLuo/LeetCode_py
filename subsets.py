"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.rst = []
        self.dfs(nums, 0,0,[])
        return self.rst
    
    def dfs(self, nums, depth, start, valuelist):
        self.rst.append(valuelist)
        if depth == len(nums): return
        for i in range(start, len(nums)):
            self.dfs(nums, depth+1, i+1, valuelist+[nums[i]])
