"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.


"""

import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] + [n]*(n) ### all by 1
        for i in range(int(math.sqrt(n))):
            dp[i*i] = 1 
        for a in range(n+1):
            b= 1
            while a+b*b <= n:
                dp[a + b*b] = min(dp[a] + 1, dp[a + b * b]);
                b += 1
        return dp[n]


class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
           #dp += min(dp[len(dp)-i*i] for i in range(1, int(math.sqrt(len(dp)+1))+1)) + 1,
                return dp[n]


        
class Solution(object):
       def numSquares(self, n):
            while n%4==0: n/=4
            if n%8==7: return 4

            for i in xrange(0,n+1):
               temp=i*i
               if temp<=n:
                    if int((n-temp)**(0.5))**2+temp==n: 
                        return 1+ (0 if temp==0 else 1)
               else:
                    break 

            return 3

