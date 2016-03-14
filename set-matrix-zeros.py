"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

### time O(m*n), space O(m+n)
class Solution:
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
    def setZeroes(self, matrix):
        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for i in range(rownum)]
        col = [False for i in range(colnum)]
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(rownum):
            for j in range(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0


#### time O(m*n), space O(1)
class Solution:
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    time O(m*n), space O(1)
    """
    def setZeroes(self, matrix):
        first_row_has_zero = False
        first_column_has_zero = False
        m, n = len(matrix), len(matrix[0])
        
        for inx in range(n):
            if matrix[0][inx] == 0:
                first_row_has_zero = True
                break
        for inx in range(m):
            if matrix[inx][0] == 0:
                first_column_has_zero = True
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_has_zero:
            for inx in range(n):
                matrix[0][inx] = 0
        
        if first_column_has_zero:
            for inx in range(m):
                matrix[inx][0] = 0
        