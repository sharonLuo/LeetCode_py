"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""



"""
We use "last_max_reach" to keep track of the maximum distance that has been reached
 by using the minimum steps "step", whereas "max_reach" is the maximum distance
 that can be reached by using "step+1" steps. Thus, max_reach = max(i + num[i]) where 0 <= i <= last.
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        last_max_reach = 0
        max_reach = 0
        for i in range(len(nums)):
            if i > last_max_reach:
                last_max_reach = max_reach
                step += 1
            max_reach = max(max_reach, i+nums[i])
        return step        