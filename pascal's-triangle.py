
"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
### beat 70%
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        crnt_row = 1
        rst = []
        while crnt_row <= numRows:
            if crnt_row == 1:
                rst.append([1])
            elif crnt_row == 2:
                rst.append([1,1])
            else:
                prev_row = rst[crnt_row - 2]
                tmp_row = [1]
                for count in range(crnt_row - 2):
                    tmp_row.append(prev_row[count]+prev_row[count+1])
                tmp_row.append(1)
                rst.append(tmp_row)    
            crnt_row += 1        
        return rst
        
 