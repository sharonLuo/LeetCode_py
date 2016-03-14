"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        i = 1
        j = x/2 + 1
        while i <= j:
            center = (i+j)/2
            if center**2 == x:
                return center
            elif center**2 > x:
                j = center-1
            else:
                i = center+1
        return j
            
            