
#You are climbing a stair case. It takes n steps to reach to the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

import math

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_of_one = n
        count_of_two = 0
        rst = 0
        while count_of_one >= 0:
            rst += math.factorial(count_of_one+count_of_two)/math.factorial(count_of_one)/math.factorial(count_of_two)
            count_of_one -= 2
            count_of_two += 1
        return rst
    

import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_of_one = n
        count_of_two = 0
        rst = 0
        while count_of_one >= 0:
            if count_of_two == 0 or count_of_one == 0:
                rst += 1
            elif count_of_two == 1:
                rst += count_of_one + 1
            elif count_of_one == 1:
                rst += count_of_two + 1
            else:
                rst += math.factorial(count_of_one+count_of_two)/math.factorial(count_of_one)/math.factorial(count_of_two)
            count_of_one -= 2
            count_of_two += 1
        return rst
    
       