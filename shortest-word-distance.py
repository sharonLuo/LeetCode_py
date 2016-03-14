"""

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""


        

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_length = len(words)
        pos1, pos2 = -1, -1
        for i in range(len(words)):
            if words[i]==word1: pos1 = i
            if words[i]==word2: pos2 = i
            if pos1!=-1 and pos2!=-1:
                min_length = min(min_length, abs(pos1-pos2))
        return min_length
        

