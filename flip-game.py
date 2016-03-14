"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]
If there is no valid move, return an empty list [].
"""

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(1, len(s)):
            if s[i]==s[i-1]=='+':
                result.append(s[:i-1]+"--"+s[i+1:])
        return result
        

        
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        plus_inx = []
        for inx in range(len(s)):
            if s[inx] == "+":
                plus_inx.append(inx)
        rst = []
        for i in range(0, len(plus_inx)-1):
            if plus_inx[i+1]-plus_inx[i] == 1:
                if plus_inx[i]+2 < len(s):
                    tmp = s[:plus_inx[i]] + "--" + s[plus_inx[i]+2:]
                else:
                    tmp = s[:plus_inx[i]] + "--"
                rst.append(tmp)
        return rst
    
