"""
用一个哈希表, 记录每个元素是否使用, 对每个元素, 以该元素为中心, 往左右扩张, 直到不连续为止, 记录下最长的长度(当一个元素被包含在长度之内, 删掉它节省时间)
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        d = {}
        for element in nums:
            if element not in d:
                d[element] = 1
        longest = 0
        for element in nums:
            length = 1
            if element not in d:
                continue
            c = element
            while element-1 in d:
                element -= 1
                length += 1
                del d[element]
            element = c
            while element+1 in d:
                element += 1
                length += 1
                del d[element]
            longest = max(longest, length)
        return longest
   