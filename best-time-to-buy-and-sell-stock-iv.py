"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if 2*k >= len(prices):
            maxprofit = 0
            for inx in range(1,len(prices)):
                if prices[inx]-prices[inx-1] > 0:
                    maxprofit += prices[inx]-prices[inx-1]
            return maxprofit
        else:
            dp = [None] * (2*k+1)
            dp[0] = 0
            for i in range(len(prices)):  ### i, from day0, day1, ...
                for j in range(1, min(2*k, i+1)+1):  ### at day i, at most min(2k, i+1) 次操作
                    dp[j] = max(dp[j], dp[j-1]+prices[i]*[1,-1][j%2])
            return dp[2*k]
###################################################

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if k*2 >= size:
            return self.noKLimit(size, prices)
        dp = [None] * (2*k+1)
        dp[0] = 0
        for i in range(size):
            for j in range(1, min(2*k, i+1)+1):
                dp[j] = max(dp[j], dp[j-1]+prices[i]*[1, -1][j%2])
        return dp[2*k]
            
    def noKLimit(self, size, prices):
        sum = 0
        for i in range(size - 1):
            if prices[i+1]>prices[i]:
                sum += prices[i+1] - prices[i]
        return sum
 
