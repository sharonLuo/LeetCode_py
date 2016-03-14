"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                tmp=board[i][j]
                board[i][j]='D' # change to any character not in 1-9 would work
                if self.isValid(board, i,j,tmp)==False: 
                    return False
                else:
                    board[i][j]=tmp
        return True
    
    def isValid(self, board, x, y, tmp):
            for i in range(9): # check column
                if board[i][y]==tmp:return False
            for i in range(9): # check row
                if board[x][i]==tmp:return False
            for i in range(3): # check current sub-boxes
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
            return True
