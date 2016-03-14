"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

(power = 1): 5, 10, 15, 20, 25, 30, ...
(power = 2): 25, 50, 75, 100, ...
(power = 3): 125, 250, ...
"""

     

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        power = 1
        while n/(5 ** power):
            count += n/(5 ** power)
            power += 1
        return count
        
        
        
