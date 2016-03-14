"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not (s[i].isalpha() or s[i].isdigit()):
                i += 1
            while j > i and not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i+1, j-1
        return True
    
      

"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_lower = s.lower()
        base_a = ord("a")
        rst = True
        if len(s_lower):
            begin = 0
            end = len(s_lower)-1
            while begin < end:
                while begin < end and not self.isNumberLetter(s_lower[begin]):
                    begin += 1
                while end > begin and not self.isNumberLetter(s_lower[end]):
                    end -= 1
                if s_lower[begin] != s_lower[end]:
                    return False
                begin += 1
                end -= 1
        return rst
        
    def isNumberLetter(self,element):
        rst = False
        if ord(element)-ord("a") >= 0 and ord(element)-ord("z") <= 0:
            rst = True
        if ord(element)-ord("0") >= 0 and ord(element)-ord("9") <= 0:
            rst = True
        return rst
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

    
       
    
