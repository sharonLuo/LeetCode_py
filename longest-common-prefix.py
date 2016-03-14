"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

##### 横向扫描
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        pref = strs[0]
        min_length = len(pref)
        for ele in strs:
            min_length = min(min_length, len(ele))
            if min_length == 0:
                return ""
            inx = 0
            for inx in range(0, min_length):
                if ele[inx] != pref[inx]:
                    min_length = inx
                    break
        return pref[:min_length]



##### 纵向扫描
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        inx = 0
        while inx < len(strs[0]):
            p = strs[0][inx]
            for element in strs:
                if len(element) <= inx or element[inx] != p:
                    return strs[0][:inx]
            inx += 1
        return strs[0][:inx]
                