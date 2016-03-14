"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""

### LinkedIn

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_length = len(words)
        if word1 == word2:
            dir = -1
            pos1, pos2 = -1, -1
            for i in range(len(words)):
                if dir == -1:
                    if words[i] == word1:
                        pos1 = i
                        dir = 1
                else:
                    if words[i] == word2:
                        pos2 = i
                        dir = -1
                if pos1!= -1 and pos2 != -1:
                    min_length = min(min_length, abs(pos1-pos2))
            return min_length
        else:
            pos1, pos2 = -1, -1
            for i in range(len(words)):
                if words[i]==word1: pos1 = i
                if words[i]==word2: pos2 = i
                if pos1!=-1 and pos2!=-1:
                    min_length = min(min_length, abs(pos1-pos2))
            return min_length
        

       
#####################
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.mapping = {}
        self.indices = {}
        for i in range(len(words)):
            self.indices[words[i]] = self.indices.get(words[i], [])
            self.indices[words[i]].append(i)
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        s = [word1, word2]
        s.sort()
        if (s[0], s[1]) in self.mapping:
            return self.mapping[(s[0], s[1])]
        if word1 not in self.indices or word2 not in self.indices:
            return -1
        pos1, pos2 = 0, 0
        min_dist = abs(self.indices[word1][pos1]-self.indices[word2][pos2])
        while pos1<len(self.indices[word1]) and pos2<len(self.indices[word2]):
            dist = self.indices[word1][pos1]-self.indices[word2][pos2]
            min_dist = min(min_dist, abs(dist))
            if dist==0:
                return min_dist
            if dist>0:
                pos2 += 1
            else:
                pos1 += 1
            
        self.mapping[(s[0],s[1])] = min_dist
        return min_dist

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")

