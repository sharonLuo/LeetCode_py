"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        low = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < low: low = prices[i]
            maxprofit = max(maxprofit, prices[i] - low)
        return maxprofit
            