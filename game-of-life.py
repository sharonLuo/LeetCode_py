"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

"""


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dx = (1, 1, 1, 0, 0, -1, -1, -1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for x in range(len(board)):
            for y in range(len(board[0])):
                lives = 0
                for z in range(8):
                    nx, ny = x + dx[z], y + dy[z]
                    lives += self.getCellStatus(board, nx, ny)
                # save the new status on higher bit    
                if lives + board[x][y] == 3 or lives == 3:
                    board[x][y] |= 2
        # right shift 1 bit to get the new status           
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] >>= 1
                
    def getCellStatus(self, board, x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return 0
        ### since 已更新的cell可能会大于1的值, 因此bit 与 with 1
        return board[x][y]&1     