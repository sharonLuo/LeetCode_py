import math

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
           if n & 1 == 1:
               count += 1
           n = n >> 1
        return count
    
        
import math

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 1:
           factor = int(math.log(n, 2))
           n -= 2 ** factor
           count += 1
        if n == 1:
            count += 1
        return count
    
        
        