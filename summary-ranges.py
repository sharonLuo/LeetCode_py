"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rst = []
        inx = 0
        while inx < len(nums):
            tmp = str(nums[inx])
            begin = inx
            while inx< len(nums)-1 and nums[inx+1]-nums[inx] == 1:
                inx += 1
            if begin != inx:
                tmp += "->" + str(nums[inx])        
            rst.append(tmp)
            inx += 1
        return rst    
 
