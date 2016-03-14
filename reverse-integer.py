"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:  
    # @return an integer  
    def reverse(self, x):  
        if x<0:  
            sign = -1  
        else:  
            sign = 1  
        strx=str(abs(x))  
        r = strx[::-1]  
        rst = sign*int(r)
        if rst <  -2**31 or rst >= 2**31:
            return 0
        return rst



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new_x = 0
        if x >= 0:
            sign = 1
        else:
            sign = -1
            x = -x
           
        while x != 0:
            new_x = new_x * 10 + x % 10
            x = x / 10
        if sign*new_x >= 2147483647 or sign*new_x < -2147483648:
            return 0
        else:
            return sign*new_x     