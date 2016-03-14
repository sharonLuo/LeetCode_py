

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""

### beat 67%
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        rst = 0
        if len(s) > 0:
            i = len(s)-1
            while i >= 0:
                if not s[i].isspace():
                    rst += 1
                else:
                    if rst != 0:
                        break
                i -= 1
        return rst
        

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        inx = size-1
        while inx >= 0 and s[inx] == " ":
            inx -= 1
        if inx == -1:
            return 0
        end_word_inx = inx
        while inx >= 0 and s[inx] != " ":
            inx -= 1
        return end_word_inx - inx
        
            
            

### beat 30%
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = s.split()
        if len(word_list) == 0:
            return 0
        else:
            return len(word_list[len(word_list)-1])
        