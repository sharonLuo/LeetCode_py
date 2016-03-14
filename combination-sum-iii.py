"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

"""



class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        Solution.rst = []
        self.DFS(k, n, 1, [])
        return Solution.rst
    
    def DFS(self, k, target, start, valuelist):
        if target == 0 and len(valuelist)==k:
            return Solution.rst.append(valuelist)
        for i in range(start, 10):
                if target < i:
                    return
                self.DFS(k, target-i, i+1, valuelist+[i])
          