"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        mid = n/2
        # rotate wrt the central line
        for inx in range(mid):
            tmp = matrix[inx]
            matrix[inx] = matrix[n-1-inx]
            matrix[n-1-inx] = tmp
        
        for i in range(1, n):
            for j in range(0, i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        mid = n/2
        # rotate wrt the central line
        for inx in range(mid):
            matrix[inx], matrix[n-1-inx] = matrix[n-1-inx], matrix[inx]

        for i in range(1, n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
