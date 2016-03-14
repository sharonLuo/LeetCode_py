
"""
Determine whether an integer is a palindrome. Do this without extra space.
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""


###### 为了避免倒置可能出现的溢出现象, 最好是不断取第一位和最后一位(10进制下)进行比较, 相等则取第二位和倒数第二位, 
###### 直到完成比较, 或者中途找到不一致的位为止

import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        divider = 1
        while x/divider >= 10:
            divider *= 10
        
        while x > 0:
            p = x/divider
            q = x%10
            if p != q:
                return False
            x = x%divider/10
            # 或者 x = (x- (q + p*divider))/10
            divider /= 100
        return True
        
    
        

### beat 90%, but use extra space
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        head = 0
        tail = len(x)-1
        while head < tail:
            if x[head] != x[tail]:
                return False
            head += 1
            tail -= 1
        return True
   