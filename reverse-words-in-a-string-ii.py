"""
Question: Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces and the words are always separated by a single space.
For example,
Given s = "the sky is blue",
return "blue is sky the".
Could you do it in-place without allocating extra space?

Idea: Reverse twice, both in place.

Time: O(n) Space: O(1)

"""

class Solution(object):
	def reverseWords(self, s):
		self.reverse(s, 0, len(s)-1)
		while i < len(s):
			j = i
			while j < len(s) and s[j] != " ":
				j += 1
			self.reverse(s[i,j], i, j)
		return s	


	def reverse(self, s, begin, end):
		mid = (end-begin)/2
		for inx in range(0, mid+1):
			s[begin+inx], s[end-inx] = s[end-inx], s[begin+inx]
		return s    
