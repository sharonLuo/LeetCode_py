
"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

#### Iterative Solution 1
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    """
    :type ratings: List[int]
    :rtype: int
    """
    def candy(self, ratings):
        candynum = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candynum[i] = candynum[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                candynum[i] = max(candynum[i+1] + 1, candynum[i])
        return sum(candynum)
        


#### Iterative Solution 2
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    """
    :type ratings: List[int]
    :rtype: int
    """
    def candy(self, ratings):
        candynum = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candynum[i] = candynum[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i+1] < ratings[i] and candynum[i+1] >= candynum[i]:
                candynum[i] = candynum[i+1] + 1
        return sum(candynum)
  
### Recursive solution  
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    """
    :type ratings: List[int]
    :rtype: int
    """
    def candy(self, ratings):
        size = len(ratings)
        ind_candy = [0]*size
        Sum = 0
        for inx in range(size):
            Sum += self.solve(ratings, ind_candy, inx)
        return Sum
    
    def solve(self, ratings, ind_candy, inx):
        if ind_candy[inx] == 0:
            ind_candy[inx] = 1
            if inx > 0 and ratings[inx] > ratings[inx-1]:
                ind_candy[inx] = max(ind_candy[inx], self.solve(ratings, ind_candy, inx-1)+1)
            if inx < len(ratings)-1 and ratings[inx] > ratings[inx+1]:
                ind_candy[inx] = max(ind_candy[inx], self.solve(ratings, ind_candy, inx+1)+1)
        return ind_candy[inx]
        

       
