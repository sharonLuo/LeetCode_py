
"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Hint:

Consider the palindromes of odd vs even length. What difference do you notice?
Count the frequency of each character.
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mp = {}
        for char in s:
            mp[char] = mp.get(char, 0) + 1
        
        ##
        odd_count = 0
        for key in mp:
            if mp[key] % 2:
                odd_count += 1
            if odd_count > 1:
                break
        return odd_count < 2



class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mp = {}
        for char in s:
            mp[char] = mp.get(char, 0) + 1
        
        tmp = [key for key in mp if mp[key]%2==1]
        return len(tmp)<= 1