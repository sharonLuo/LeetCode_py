"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""

###### simpler method
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        stack = []
        i = 0
        maxArea = 0
        h = height + [0]
        h_length = len(h)
        while i < h_length: 
            # not stack means stack is empty
            if (not stack) or h[stack[-1]] <= h[i]:
                stack.append(i) ### stack 不是严格递增, 相同的4,4 都会被压入栈
                i += 1
            else:
                t = stack.pop()
                ### since pop first, so the width = i-stack[-1]-1 
                maxArea = max(maxArea, h[t] * (i if not stack else i - stack[-1] - 1))
        return maxArea


### define stack as (height, inx)
class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        answer = 0
        if len(height) == 0:
            return 0
        if len(height) == 1:
            return height[0]
        stack = [(height[0], 0)]
        for inx in range(1,len(height)):
            if height[inx] > stack[-1][0]:
                stack.append([height[inx], inx])
            elif height[inx] == stack[-1][0]:
                continue
            else:
                while stack != [] and height[inx] < stack[-1][0]:
                    answer = max(answer, stack[-1][0]*(inx-stack[-1][1]))
                    leftsize = stack[-1][1]
                    stack.pop()
                stack.append([height[inx], leftsize])
        # now the stack is stickly increasing
        last = inx+1
        while stack != []:
            answer = max(answer, stack[-1][0]*(last-stack[-1][1]))
            stack.pop()
        return answer

                
