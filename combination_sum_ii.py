"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 

"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.rst = []
        self.DFS(candidates, target, 0, [])
        return Solution.rst
    
    def DFS(self, candidates, target, startinx, valuelist):
        endinx = len(candidates)
        if target == 0 and valuelist not in Solution.rst: 
            return Solution.rst.append(valuelist)
        for inx in range(startinx, endinx):
                if target < candidates[inx]:
                    return
                self.DFS(candidates, target-candidates[inx], inx+1, valuelist+[candidates[inx]])
  