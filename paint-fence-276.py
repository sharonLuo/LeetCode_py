

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n < 2:              ### for n = 0, 1
            return n*k
        dp1, dp2 = k, k*(k-1)  ### for n = 2
        for inx in range(2, n):
            new_dp2 = (k-1)*(dp1 + dp2)
            dp1 = dp2
            dp2 = new_dp2
        return dp1 + dp2
 

 class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n < 2:
            return n*k
        dp1, dp2 = k, k*(k-1)
        for inx in range(2, n):
            new_dp1 = dp2
            dp2 = (k-1)*(dp1+dp2)
            dp1 = new_dp1
        return dp1 + dp2
            
            
  