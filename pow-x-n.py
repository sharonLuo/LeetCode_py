"""
Implement pow(x, n).
"""



class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == -1:
            return 1/x
        elif n == 1:
            return x
        elif n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return self.myPow(x*x, (n-1)/2)*x
        