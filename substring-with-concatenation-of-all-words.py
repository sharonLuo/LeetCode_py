"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        d = {}
        for i in words:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        wordNum, wordLen = len(words), len(words[0])
        res = []
        for i in range(len(s)+1-wordLen*wordNum): ### beyond that not enough space
            curr = {}
            j = 0 ### number of word matched
            while j < wordNum:
                word = s[i+j*wordLen:i+j*wordLen+wordLen]
                if word not in words:
                    break
                if word not in curr:
                    curr[word] = 1
                else:
                    curr[word] += 1
                if curr[word] > d[word]:
                    break
                j += 1
            if j == wordNum:
                res.append(i)
        return res
        
            
        
        