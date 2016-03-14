"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

### O(m+n) 从左下角扫到右上角
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ### from bottom-left to top-right
        if matrix == []:
            return False
        row, col = len(matrix)-1, 0
        while row >=0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False

#### O(m*log(n)) 循环枚举行, 二分查找列
class Solution(object):
    def binSearch(self, nums, low, high, target):
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        
    def searchMatrix(self, matrix, target):
        y = len(matrix[0]) - 1
        for x in range(len(matrix)):
            y = self.binSearch(matrix[x], 0, y, target)
            if matrix[x][y] == target:
                return True
        return False    


 ### O(m+n) 从右上角扫到左下角
 class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ### from top-right to bottom-left
        if matrix == []:
            return False
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

                
                
            
                       
            
        

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        top, down = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        if target < matrix[0][0] or target > matrix[down][right]:
            return False
            
        while top <= down:
            mid = (top+down)/2
            if matrix[mid][0] < target:
                top = mid+1
            elif matrix[mid][0] > target:
                down = mid-1
            else:
                return True
        if len(matrix[0]) == 1 and top > down: 
            return False
        else:### mark the last row satisfying first element < target
            checkrow = top-1
            
        left, right = 0, len(matrix[0])-1
        while left <= right:
            mid = (left + right)/2
            if matrix[0][mid] < target:
                left = mid+1
            elif matrix[0][mid] > target:
                right = mid-1
            else:
                return True
        if len(matrix) == 1 and left > right:
            return False
        else:### mark the first row satisifying last element > target
            checkcolumn = left-1
        print checkrow, checkcolumn
        
        for row_inx in range(0, checkrow+1):
            left, right = 0, checkcolumn
            while left <= right:
                mid = (left+right)/2
                if matrix[row_inx][mid] == target:
                    return True
                elif matrix[row_inx][mid] < target:
                    left = mid+1
                else:
                    right = mid-1
        return False
            
        
                
                
            
        