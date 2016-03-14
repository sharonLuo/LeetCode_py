"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

"""
For ABCDEFGHIJKLMN
2-"ACEGIKMBDFHJLN"
4-"AGMBFHLNCEIKDJ"
5-

"""
class Solution:
    def convert(self, s, nRows):
        step, zigzag = 2*(nRows-1), ""
        if s == None or len(s) == 0 or nRows <= 0:
            return ""
        if nRows == 1:
            return s
        for i in range(nRows):
            for j in range(i, len(s), step):
                zigzag += s[j]
                if i > 0 and i < nRows - 1 and j+step-2*i < len(s):
                    zigzag += s[j+step-2*i]
        return zigzag





class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rst = ""
        if numRows == 1:
            rst = s
        else:
            for inx in range(0, min(numRows,len(s))):
                if inx == 0 or inx == (numRows-1):
                    rst = rst + s[inx::2*(numRows-1)]
                else:
                    s1 = s[inx::2*(numRows-1)]
                    s2 = s[2*(numRows-1)-(inx)::2*(numRows-1)]
                    len_s1 = len(s1)
                    len_s2 = len(s2)
                    if len_s2 == 0:
                        rst += s1
                    else:
                        for inx2 in range(0,(len_s1-1)):
                            rst += s1[inx2]
                            rst += s2[inx2]
                        rst += s1[len_s1-1]
                        if len_s2 == len_s1:
                            rst += s2[len_s1-1]
        return rst


"""
For ABCDEFGHIJKLMN
2-"ACEGIKMBDFHJLN"
4-"AGMBFHLNCEIKDJ"
5-

"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rst = ""
        if numRows == 1:
            rst = s
        else:
            for inx in range(0, min(numRows,len(s))):
                if inx == 0 or inx == (numRows-1):
                    rst += s[inx::2*(numRows-1)]
                else:
                    s1 = s[inx::2*(numRows-1)]
                    s2 = s[2*(numRows-1)-(inx)::2*(numRows-1)]
                    len_s1 = len(s1)
                    len_s2 = len(s2)
                    for inx2 in range(0,(len_s1)):
                            rst += s1[inx2]
                            if inx2 < len_s2:
                                rst += s2[inx2]
        return rst
    
          
 
    
