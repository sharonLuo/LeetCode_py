"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        length = len(words)
        nums = [0]*length
        for i, element in enumerate(words):
            nums[i] = sum(1 << (ord(x)-ord('a')) for x in set(element))
        maxlength = 0
        for i in range(length):
            for j in range(i+1, length):
                if nums[i]&nums[j] == 0 and len(words[i])*len(words[j]) > maxlength:
                    maxlength = len(words[i])*len(words[j])
        return maxlength
 


#### same idea as above
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        length = len(words)
        nums = [0]*length
        for i, element in enumerate(words):
            for x in element:
                nums[i] |= 1 << (ord(x)-ord('a'))
        maxlength = 0
        for i in range(length):
            for j in range(i+1, length):
                if nums[i]&nums[j] == 0 and len(words[i])*len(words[j]) > maxlength:
                    maxlength = len(words[i])*len(words[j])
        return maxlength
        

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        es = [set() for x in range(26)]
        ml = collections.defaultdict(int)
        for w in words:
            num = sum(1<<(ord(x)-ord('a')) for x in set(w))
            ml[num] = max(ml[num], len(w))
            for x in set(string.lowercase)-set(w):
                es[ord(x)-ord('a')].add(num)
        ans = 0
        for w in words:
            r = [es[ord(x)-ord('a')] for x in w]
            if not r: continue
            r = set.intersection(*r)
            for x in r:
                ans = max(ans, len(w)*ml[x])
        return ans
     
        
            
                      
            


            