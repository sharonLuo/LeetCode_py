"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

"""


###### Approach (1) for every element as center, look left and right to find palindrom, watch out "abba", and "aba" difference
class Solution(object):
    def searchPalindrome(self, s, rst, left, right):
    	size = len(s)
    	while left >= 0 and right < size and s[left]==s[right]:
    		left -= 1
    		right += 1
    	tmp = s[max(0, left+1):min(right-1, size-1)+1]
    	if len(tmp) > len(rst):
    		rst = tmp
    	return rst
 
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        rst = ""
        for inx in range(size):
            ### first even length 
            rst = self.searchPalindrome(s, rst, inx, inx)
            ### next odd length
            rst = self.searchPalindrome(s, rst, inx, inx+1)
        return rst



                    
######  Dynamic Programming (TLE for python on Leetcode)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        ### create a table to store results of subproblems
        L = [[0 for x in range(size)] for x in range(size)]
        
        ### strings of length 1 are palindrome of length 1
        for i in range(size):
            L[i][i] = 1
        """
        build the table. Note that the lower triangle values of table are useless and not filled in the process. length is the length of substring to be considered
        """
        max_i, max_j = 0, 0
        for length in range(2, size+1):
            for i in range(size-length+1):
                j = i+length -1
                if s[i] == s[j] and length == 2:
                    L[i][j] = 1
                if s[i] == s[j] and length > 2:
                    L[i][j] = L[i+1][j-1]
                if L[i][j] == 1 and j - i > (max_j-max_i):
                    max_i, max_j = i, j
        return s[max_i:max_j+1]


#########
# Manacher's Algorithm
# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
# http://www.felix021.com/blog/read.php?2040
# ~O(n)
def longest_palin_substr5(s):
    # reformat the string
    s = list(s)
    # so that all the palindrome substrings are of odd length
    for i in range(len(s)+1): s.insert(i*2,'#')
    print s
    p = defaultdict(int) # left/right length of palindrome centered at s[i]
    max_center = 0 # current maximum palindrom's center
    max_upper = 0 # maximum palindrom's upper boundary, max_center+P[max_center]
    for i in range(1,len(s)):
        # i & j are symmetric points to max_center_id
        j = 2*max_center - i
        p[i] = min(p[j], max_upper-i) if max_upper > i else 1
        while i-p[i] >= 0 and i+p[i] <= len(s)-1 and s[i+p[i]] == s[i-p[i]]: 
            p[i]+=1
        if p[i]+i > max_upper:
            max_upper = p[i]+i
            max_center = i
    print 's:', ','.join(s)
    print 'p:', ','.join(map(str, [p[i] for i in range(len(s))]))
    return max(p.values())-1


    
 """      
 #### similar as approach (1) 
 class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        rst = ""
        ### first even length 
        inx = 0
        while inx < size-1:
            if s[inx] == s[inx+1]:
                left = inx-1
                right = inx+2
                while left >=0 and right < size and s[left]==s[right]:
                    left -= 1
                    right += 1
                tmp = s[max(0, left+1):min(right-1, size-1)+1]
                if len(tmp)>len(rst):
                    rst = tmp
            inx += 1  
        
        ### next odd length
        inx = 0
        while inx < size:
            left = inx-1
            right = inx+1
            while left >=0 and right < size and s[left]==s[right]:
                left -= 1
                right += 1
            tmp = s[max(0, left+1):min(right-1, size-1)+1]
            if len(tmp)>len(rst):
                rst = tmp
            inx += 1
        return rst

#### Similary as approach 1
class Solution(object):
    def searchPalindrome(self, s, rst, inx1, inx2):
    	size = len(s)
    	left = inx1-1
    	right = inx2+1
    	while left >= 0 and right < size and s[left]==s[right]:
    		left -= 1
    		right += 1
    	tmp = s[max(0, left+1):min(right-1, size-1)+1]
    	if len(tmp) > len(rst):
    		rst = tmp
    	return rst
 
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        rst = ""
        ### first even length 
        inx = 0
        while inx < size-1:
            if s[inx] == s[inx+1]:
                rst = self.searchPalindrome(s, rst, inx, inx+1)
            inx += 1  
        ### next odd length
        inx = 0
        while inx < size:
            rst = self.searchPalindrome(s, rst, inx, inx)
            inx += 1
        return rst
"""        
