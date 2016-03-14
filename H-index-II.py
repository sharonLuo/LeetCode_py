"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right, size = 0, len(citations), len(citations)
        while left < right:
            mid = (left+right)/2
            if citations[mid] >= size - mid:
                right = mid
            else:
                left = mid + 1
        return size - left