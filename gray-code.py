"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""

# by property of gray code
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        rst = [i for i in range(2**n)]
        for i in range(len(rst)):
            rst[i] = (rst[i]>>1)^(rst[i])
        return rst


# by recursive approach
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        rst = [0,1]
        m = 2
        while m <= n:
            base = 2**(m-1)
            for inx in range(base-1, -1, -1):
                rst.append(rst[inx] + 2**(m-1))
            m += 1
        return rst
        
    