"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lefts = {'(':0, '[':1, '{':2}
        rights = {')':0, ']':1, '}':2}
        stack = []
        for ch in s:
            if ch in lefts:
                stack.append(lefts[ch])
            elif ch in rights:
                if not stack: 
                    return False
                if stack[-1] == rights[ch]: 
                    stack.pop()
                else:
                    return False
        return not stack
    
                
