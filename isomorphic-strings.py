
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""



### beat 80%
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = t[i]
            else:
                if d[c] != t[i]:
                    return False
        
        d = {}
        for i, c, in enumerate(t):
            if c not in d:
                d[c] = s[i]
            else:
                if d[c] != s[i]:
                    return False
        return True


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        d1 = {}
        d2 = {}
        for (cs, ct) in zip(s, t):
            if d1.get(cs) is None and d2.get(ct) is None:
                d1[cs] = ct
                d2[ct] = cs
            else:
                if d1.get(cs) != ct or d2.get(ct) != cs:
                    return False
        return True

