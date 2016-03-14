"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""



class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        vis, cnt = [False] * 26, [0] * 26
        ans = []
        for c in s:
            cnt[ord(c) - ord('a')] += 1  
        for c in s:
            index = ord(c) - ord('a')
            cnt[index] -= 1
            if vis[index]: continue
            while ans and ans[-1] > c and cnt[ord(ans[-1]) - ord('a')]:
                vis[ord(ans.pop()) - ord('a')] = False
            ans.append(c)
            vis[index] = True
        return ''.join(ans)        


##### 递归
def removeDuplicateLetters(self, s):
    for c in sorted(set(s)):
        suffix = s[s.index(c):]
        if set(suffix) == set(s):
            return c + self.removeDuplicateLetters(suffix.replace(c, ''))
    return ''