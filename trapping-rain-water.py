
"""
解题思路：模拟法。开辟一个数组leftmosthigh，leftmosthigh[i]为A[i]之前的最高的bar值，然后从后面开始遍历，用rightmax来记录从后向前遍历遇到的最大bar值，那么min(leftmosthigh[i], rightmax)-A[i]就是在第i个bar可以储存的水量。例如当i=9时，此时leftmosthigh[9]=3,而rightmax=2，则储水量为2-1=1，依次类推即可。这种方法还是很巧妙的。时间复杂度为O(N)。
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        size = len(height)
        left_max = [0]*size
        right_max = [0]*size
        left_max[0] = height[0]
        right_max[size-1] = height[size-1]
        
        for inx in range(1, size):
            left_max[inx] = max(left_max[inx-1], height[inx])
            right_max[size-inx-1] = max(right_max[size-inx], height[size-inx-1])
        
        rst = 0
        for inx in range(size):
            rst += min(left_max[inx], right_max[inx])-height[inx]
        return rst
        
        
            