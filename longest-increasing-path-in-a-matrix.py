"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

#### 记忆化搜索 DFS + memorization

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return -0
        m, n = len(matrix), len(matrix[0])
        dis = [[0 for _ in range(n)] for _ in range(m)]
        return max([self.dfs(i, j, m, n, matrix, dis) for j in range(n) for i in range(m)])
        
    def dfs(self, x, y, m, n, matrix, dis):
        if dis[x][y] != 0: return dis[x][y]
        else:
            for dx, dy in ([(0,1), (0,-1), (1,0), (-1,0)]):
                newx, newy = x + dx, y+dy
                if newx >= 0 and newx < m and newy >= 0 and newy < n and matrix[newx][newy] > matrix[x][y]:
                    dis[x][y] = max(dis[x][y], self.dfs(newx, newy, m, n, matrix, dis))
            dis[x][y] += 1
        return dis[x][y]
        

#### 排序 + 动态规划
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dis = [[1]*n for _ in range(m)]
        slist = sorted([(i,j,val) for i, row in enumerate(matrix) for j, val in enumerate(row)], key=operator.itemgetter(2))
        for x,y,val in slist:
            for dx, dy in ([(1,0), (-1,0), (0,-1), (0,1)]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0<= ny < n and matrix[x][y] < matrix[nx][ny]:
                    dis[nx][ny] = max(dis[nx][ny], dis[x][y]+1)
        return max(dis[x][y] for x in range(m) for y in range(n))
                

        
            
        
        
            
        