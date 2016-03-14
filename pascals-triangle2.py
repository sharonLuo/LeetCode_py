
"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        list = [[] for i in range(rowIndex+1)]
        list[0] = [1]
        list[1] = [1, 1]
        for i in range(2, rowIndex+1):
            list[i] = [1 for j in range(i + 1)]
            for j in range(1, i):
                list[i][j] = list[i - 1][j - 1] + list[i - 1][j]
        return list[rowIndex]


        
import math

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rst = []
        for x in range(rowIndex+1):
            tmp = math.factorial(rowIndex)/math.factorial(x)/math.factorial(rowIndex-x)
            rst.append(tmp)
        return rst
    
