
"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1: 
            return ""
        if n == 1:
            return "1"
        res = "1"
        for i in range(n-1):
            res = self.say(res)
        return res
    
    def say(self,s):
        res = ""
        curr = None
        for i in s:
            if i != curr:
                if curr:
                    res += str(count)+str(curr)
                curr = i
                count = 1
            else:
                count += 1
        res += str(count)+str(curr)
        return res
    

            
            
